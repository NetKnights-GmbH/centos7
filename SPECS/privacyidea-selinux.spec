%global selinuxtype	targeted
%global moduletype	services
%global modulenames	privacyidea-selinux	

# Usage: _format var format
#   Expand 'modulenames' into various formats as needed
#   Format must contain '$x' somewhere to do anything useful
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;

# Relabel files
%global relabel_files() \ # ADD files in *.fc file

# Version of distribution SELinux policy package
%if 0%{?centos_ver} == 7
%global selinux_policyver 3.13.1-266.el7
%endif
%if 0%{?centos_ver} == 8
%global selinux_policyver 3.14.3-20.el8
%endif

# Version of distribution SELinux policy package 
#%global selinux_policyver 3.14.3-20.el8

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

Source:			%{name}-%{version}.tar.gz

%description
privacyidea-selinux is a additional package 
for the RPM package privacyidea/privacyidea-server
with a SELinux policy module, that allows
httpd service the communicate with the services mysql and ldap

%prep
%setup -q

%build
make SHARE="%{_datadir}" TARGETS="%{modulenames}"

%install

# Install SELinux interfaces
%_format INTERFACES $x.if
install -d %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -p -m 644 $INTERFACES \
	%{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}

# Install policy modules
%_format MODULES $x.pp.bz2
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 0644 $MODULES \
	%{buildroot}%{_datadir}/selinux/packages

%post
#
# Install all modules in a single transaction
#
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%{_sbindir}/semodule -n -s %{selinuxtype} -i $MODULES
if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/load_policy
    %relabel_files
fi


%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/semodule -n -r %{modulenames} &> /dev/null || :
	if %{_sbindir}/selinuxenabled ; then
		%{_sbindir}/load_policy
		%relabel_files
	fi
fi

%files
%defattr(-,root,root,0755)
%attr(0644,root,root) %{_datadir}/selinux/packages/*.pp.bz2
%attr(0644,root,root) %{_datadir}/selinux/devel/include/%{moduletype}/*.if

%changelog
* Fri Jun 19 2020 Julio Storch <julio.storch@netknights.it> - 1.0.0-1
- First Build

