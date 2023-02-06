%define source_name privacyIDEA
%define name privacyidea-server
%define version %{getenv:PI_VERSION}
%define unmangled_version %{version}
%define release 1

Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        two-factor authentication server

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       Cornelius Kölbel <cornelius.koelbel@netknights.it>
ExclusiveArch:  x86_64

Requires:       privacyidea = %{version}, mariadb-server, httpd, mod_ssl, shadow-utils, rng-tools
Requires:       python3-mod_wsgi

Source1: pi.cfg
Source2: privacyideaapp.wsgi
Source3: privacyidea.conf
Source4: privacyidea-cron
# BuildRequires:

%description
 privacyIDEA: identity, multifactor authentication, authorization.
 This package contains the python module for privacyIDEA.
 This is the complete server part with MariaDB and HTTPD.


%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc/privacyidea
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d/
mkdir -p $RPM_BUILD_ROOT/etc/cron.d/
# we need to change access right, otherwise each local user could call
# pi-manage
install -m 640 %{SOURCE1} $RPM_BUILD_ROOT/etc/privacyidea
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/privacyidea
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/httpd/conf.d/
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/
##################################################
# Get the NetKnights public key and other configs
curl https://raw.githubusercontent.com/privacyidea/privacyidea/master/deploy/privacyidea/NetKnights.pem -o $RPM_BUILD_ROOT/etc/privacyidea/NetKnights.pem
curl https://raw.githubusercontent.com/privacyidea/privacyidea/master/deploy/privacyidea/dictionary -o $RPM_BUILD_ROOT/etc/privacyidea/dictionary


%clean
rm -rf $RPM_BUILD_ROOT

%files
%config(noreplace) /etc/privacyidea
%config(noreplace) /etc/httpd/conf.d
%config(noreplace) /etc/cron.d

%posttrans
# first we enable and start the rngd since creation of gpg-keys might block in VMs
systemctl enable --now rngd.service
USERNAME=privacyidea
getent passwd $USERNAME >/dev/null || useradd -r $USERNAME -m 2>&1 || true > /dev/null
mkdir -p /var/log/privacyidea
mkdir -p /var/lib/privacyidea
touch /var/log/privacyidea/privacyidea.log
source /opt/privacyidea/bin/activate
pi-manage create_enckey 2>&1 || true
pi-manage create_audit_keys 2>&1 || true
chown -R $USERNAME /var/log/privacyidea
chown -R $USERNAME /var/lib/privacyidea
chown -R $USERNAME /etc/privacyidea
chgrp root /etc/privacyidea/pi.cfg
chmod 600 /etc/privacyidea/enckey
chmod 600 /etc/privacyidea/private.pem
# we need to change access right, otherwise each local user could call
# pi-manage
chgrp root /etc/privacyidea/pi.cfg
chmod 640 /etc/privacyidea/pi.cfg

##################################################
# Adapt pi.cfg
if [ -z "$(grep ^PI_PEPPER /etc/privacyidea/pi.cfg)" ]; then
    # PEPPER does not exist, yet
    PEPPER="$(tr -dc A-Za-z0-9_ </dev/urandom | head -c24)"
    echo "PI_PEPPER = '$PEPPER'" >> /etc/privacyidea/pi.cfg
fi
if [ -z "$(grep ^SECRET_KEY /etc/privacyidea/pi.cfg)" ]; then
    # SECRET_KEY does not exist, yet
    SECRET="$(tr -dc A-Za-z0-9_ </dev/urandom | head -c24)"
    echo "SECRET_KEY = '$SECRET'" >> /etc/privacyidea/pi.cfg
fi
if [ -n "$(grep '^SQLALCHEMY_DATABASE_URI\s*=\s*.\(py\)\?mysql:.*$' /etc/privacyidea/pi.cfg)" ]; then
    #  We found an old mysql config file
    sed -i -e s/"\(^SQLALCHEMY_DATABASE_URI\s*=\s*.\)\(py\)\?mysql:\(.*\)$"/"\1mysql+pymysql:\3"/g /etc/privacyidea/pi.cfg
    echo "# The SQLALCHEMY_DATABASE_URI was updated during the update to privacyIDEA %{version}" >> /etc/privacyidea/pi.cfg
fi

#####################################################
# Create database
if [ -z "$(grep ^SQLALCHEMY_DATABASE_URI /etc/privacyidea/pi.cfg)" ]; then
    NPW="$(tr -dc A-Za-z0-9_ </dev/urandom | head -c12)"
    # might not run
    systemctl start mariadb
    # check if pi database exists
    mysql pi -e quit 2> /dev/null
    if [ $? -ne 0 ]; then
        # create the new database if it does not exist
        mysql -e "create database pi;" || true
    else
        echo "Database already exists. Good."
    fi
    mysql -e "grant all privileges on pi.* to 'pi'@'localhost' identified by '$NPW';"
    echo "SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://pi:$NPW@localhost/pi'" >> /etc/privacyidea/pi.cfg
    # pi-manage create_tables 2>&1 || true > /dev/null
    pi-manage createdb 2>&1 || true > /dev/null
fi

####################################################
# Update DB
# Upgrade the database
/opt/privacyidea/bin/privacyidea-schema-upgrade /opt/privacyidea/lib/privacyidea/migrations 2>&1 > /dev/null

###################################################
# The webserver
# first we need to create the self-signed certificates on CentOS 8.
[[ -x /usr/libexec/httpd-ssl-gencerts ]] && /usr/libexec/httpd-ssl-gencerts
# then we can disable the default configurations
cp /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf.disable 2>&1 || true > /dev/null
cp /etc/httpd/conf.d/welcome.conf /etc/httpd/conf.d/welcome.conf.disable 2>&1 || true > /dev/null
echo "# placeholder to avoid conflict with privacyidea.conf" > /etc/httpd/conf.d/ssl.conf
echo "# placeholder to avoid conflict with privacyidea.conf" > /etc/httpd/conf.d/welcome.conf
# finally restart the webserver
systemctl restart httpd

######################################################
# Create PGP key
mkdir -p /etc/privacyidea/gpg
pi-manage create_pgp_keys || true
chown -R $USERNAME /etc/privacyidea/gpg

# Create symlinks for the easy life of the admin
ln -sf /opt/privacyidea/bin/pi-manage /usr/bin/
ln -sf /opt/privacyidea/bin/privacyidea-diag /usr/bin/
ln -sf /opt/privacyidea/bin/privacyidea-token-janitor /usr/bin/

%changelog
%include %{_topdir}/changelog-server.inc
