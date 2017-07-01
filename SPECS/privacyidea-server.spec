%define source_name privacyIDEA
%define name privacyidea-server
%define version %{getenv:PI_VERSION} 
%define unmangled_version %{version}
%define unmangled_version %{version}
%define release 1
Name:           %{name}
Version:        %{version}
Release:        1%{?dist}
Summary:        two-factor authentication server

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       Cornelius Kölbel <cornelius.koelbel@netknights.it>
BuildArch:      x86_64
Requires:	privacyidea, mariadb-server, httpd, mod_wsgi, mod_ssl

BuildRequires: libxml2-devel, freetype-devel, python-devel, libxslt-devel, zlib-devel, openssl-devel

%description
 privacyIDEA: identity, multifactor authentication, authorization.
 This package contains the python module for privacyIDEA.
 This is the complete server part with MariaDB and HTTPD.


%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc/privacyidea
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d/
cp $RPM_SOURCE_DIR/pi.cfg $RPM_BUILD_ROOT/etc/privacyidea
cp $RPM_SOURCE_DIR/privacyideaapp.wsgi $RPM_BUILD_ROOT/etc/privacyidea
cp $RPM_SOURCE_DIR/privacyidea.conf $RPM_BUILD_ROOT/etc/httpd/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/etc/privacyidea
/etc/httpd/conf.d/

%post
USERNAME=privacyidea
useradd -r $USERNAME -m || true
mkdir -p /var/log/privacyidea
mkdir -p /var/lib/privacyidea
touch /var/log/privacyidea/privacyidea.log
source /opt/privacyidea/bin/activate
pi-manage create_enckey || true > /dev/null
pi-manage create_audit_keys || true > /dev/null
chown -R $USERNAME /var/log/privacyidea
chown -R $USERNAME /var/lib/privacyidea
chown -R $USERNAME /etc/privacyidea
chmod 600 /etc/privacyidea/enckey
chmod 600 /etc/privacyidea/private.pem
# we need to change access right, otherwise each local user could call
# pi-manage
chgrp root /etc/privacyidea/pi.cfg
chmod 640 /etc/privacyidea/pi.cfg
#####################################################
# Create database
if [ !$(grep "^SQLALCHEMY_DATABASE_URI" /etc/privacyidea/pi.cfg || true) ]; then
	service mariadb restart
	NPW="$(tr -dc A-Za-z0-9_ </dev/urandom | head -c12)"
	mysql -e "create database pi;" || true
        mysql -e "grant all privileges on pi.* to 'pi'@'localhost' identified by '$NPW';"
        echo "SQLALCHEMY_DATABASE_URI = 'pymysql://pi:$NPW@localhost/pi'" >> /etc/privacyidea/pi.cfg
fi
pi-manage createdb || true > /dev/null
####################################################
# Update DB
# Set the version to the first PI 2.0 version
pi-manage db stamp 4f32a4e1bf33 -d /opt/privacyidea/lib/privacyidea/migrations > /dev/null
# Upgrade the database
pi-manage db upgrade -d /opt/privacyidea/lib/privacyidea/migrations > /dev/null

###################################################
# The webserver
mkdir -p /var/run/wsgi
mv /etc/httpd/conf.d/welcome.conf /etc/httpd/conf.d/welcome.conf.disable
mv /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf.disable

%changelog
%include %{_topdir}/changelog-server.inc
