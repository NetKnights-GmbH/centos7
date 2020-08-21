%global selinuxtype	targeted
%global moduletype	services
%global modulenames	privacyidea-selinux	

# Usage: _format var format
# Expand 'modulenames' into various formats as needed
# Format must contain '$x' somewhere to do anything useful
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;

# Version of distribution SELinux policy package
%if 0%{?centos_ver} == 7
%global selinux_policyver 3.13.1-266.el7
%endif
%if 0%{?centos_ver} == 8
%global selinux_policyver 3.14.3-20.el8
%endif

# Package information
Name:			privacyidea-selinux
Version:		1.0	
Release:		1%{?dist}
License:		GPLv2
Group:			System Environment/Base
Summary:		SELinux Policy for privacyidea privacyidea-server 
BuildArch:		noarch
URL:			https://privacyidea.org
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, libselinux-utils
BuildRequires:		selinux-policy selinux-policy-devel
Source1:		privacyidea-selinux-src

%description
privacyidea-selinux provides a SELinux polices module
for using with the privacyidea/ privacyidea-server packages
based on Centos OS, that allows httpd service
communicate with the services mysql and ldap

%prep
rm -rf %{_builddir}/%{name}-%{version}
cp -r %{SOURCE1} %{_builddir}/%{name}-%{version}

%build
cd %{_builddir}/%{name}-%{version}
make SHARE="%{_datadir}" TARGETS="%{modulenames}"

%pre
%selinux_relabel_pre -s %{selinuxtype}

%install
# Create directories where SELinux polies will be installed
install -d %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -d %{buildroot}%{_datadir}/selinux/packages

# Install SELinux interfaces
%_format INTERFACES $x.if
cd %{_builddir}/%{name}-%{version}
install -p -m 644 $INTERFACES %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}

# Install policy modules
%_format MODULES $x.pp.bz2
cd %{_builddir}/%{name}-%{version}
install -m 0644 $MODULES %{buildroot}%{_datadir}/selinux/packages

%post
# Install all modules in a single transaction
# use selinux_set_booleans after custom SELinux module is loaded.
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%selinux_modules_install -s %{selinuxtype} $MODULES
semanage fcontext -a -t httpd_log_t "/var/log/privacyidea/privacyidea.log*"
restorecon -R -v /var/log > /dev/null 2>&1

%postun
# Uninstall module
if [ $1 -eq 0 ]; then 
%selinux_modules_uninstall -s %{selinuxtype} privacyidea-selinux
fi
semanage fcontext -d "/var/log/privacyidea/privacyidea.log*"
restorecon -R -v /var/log > /dev/null 2>&1

%posttrans
%selinux_relabel_post -s %{selinuxtype}

%files
%defattr(0644,root,root,0755)
%{_datadir}/selinux/packages/*.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/*.if

%changelog
* Fri Jun 19 2020 Julio Storch <julio.storch@netknights.it> - 1.0.0-1
- First Build
