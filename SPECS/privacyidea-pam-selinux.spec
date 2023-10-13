%global selinuxtype	targeted
%global moduletype	services
%global modulenames	privacyidea-pam-selinux
%define release 1

# Usage: _format var format
# Expand 'modulenames' into various formats as needed
# Format must contain '$x' somewhere to do anything useful
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;

# Package information
Name:			privacyidea-pam-selinux
Version:		1.0	
Release:		%{release}%{?dist}
License:		GPLv2
Group:			System Environment/Base
Summary:		SELinux Policy for pam-privacyidea.so module 
BuildArch:		noarch
URL:			https://privacyidea.org
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, libselinux-utils
BuildRequires:		selinux-policy selinux-policy-devel
Source1:		privacyidea-pam-selinux-src

%description
privacyidea-pam-selinux provides an SELinux policy module
for use with the privacyIDEA server that allows the pam module 
to communicate correctly with the privacyIDEA sever.

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

%postun
# Uninstall module
[[ $1 -eq 0 ]] && %selinux_modules_uninstall -s %{selinuxtype} privacyidea-pam-selinux
[[ -e /var/log/privacyidea ]] && restorecon -R -v /var/log/privacyidea > /dev/null 2>&1

%posttrans
%selinux_relabel_post -s %{selinuxtype}

%clean
rm -rf %{_builddir}

%files
%defattr(0644,root,root,0755)
%{_datadir}/selinux/packages/*.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/*.if

%changelog
* Tue Sep 26 2023 Julio Storch <julio.storch@netknights.it> - 1.0.0-1
- SElinux PAM build release
