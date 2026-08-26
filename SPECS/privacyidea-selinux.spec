%global selinuxtype targeted
%global moduletype services
%global modulenames privacyidea-selinux
%global release 4

# Usage: _format var format
# Expand 'modulenames' into various formats as needed.
# Format must contain '$x'.
%global _format() export %1=""; for x in %{modulenames}; do %1+="%2 "; done

Name:           privacyidea-selinux
Version:        1.0
Release:        %{release}%{?dist}
License:        GPLv2
Group:          System Environment/Base
Summary:        SELinux policy for privacyIDEA
BuildArch:      noarch
URL:            https://privacyidea.org

BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel

%{?selinux_requires}

Source1:        privacyidea-selinux-src

%description
privacyidea-selinux provides an SELinux policy module for
privacyIDEA running on Red Hat Enterprise Linux and compatible
distributions.

The policy allows privacyIDEA running in the httpd_t domain
to connect to LDAP and MySQL/MariaDB services and assigns
the correct SELinux file context to /var/log/privacyidea.

%prep
rm -rf %{_builddir}/%{name}-%{version}
cp -r %{SOURCE1} %{_builddir}/%{name}-%{version}

%build
cd %{_builddir}/%{name}-%{version}
make SHARE="%{_datadir}" TARGETS="%{modulenames}"

%pre
%selinux_relabel_pre -s %{selinuxtype}

%install
# Create directories for SELinux policy modules and interfaces.
install -d %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -d %{buildroot}%{_datadir}/selinux/packages

# Install SELinux interfaces.
%_format INTERFACES $x.if
cd %{_builddir}/%{name}-%{version}
install -p -m 0644 $INTERFACES \
    %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}

# Install SELinux policy modules.
%_format MODULES $x.pp.bz2
cd %{_builddir}/%{name}-%{version}
install -m 0644 $MODULES \
    %{buildroot}%{_datadir}/selinux/packages

%post
# Install the SELinux policy module.
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%selinux_modules_install -s %{selinuxtype} $MODULES

# Apply the newly installed file context to an existing privacyIDEA
# log directory and its files.
if [ -d /var/log/privacyidea ]; then
    restorecon -R /var/log/privacyidea || :
fi

%postun
# Remove the SELinux policy module only when the package itself
# is removed, not during an upgrade.
if [ "$1" -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} privacyidea-selinux
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}

%files
%defattr(0644,root,root,0755)
%{_datadir}/selinux/packages/*.pp.bz2
%{_datadir}/selinux/devel/include/%{moduletype}/*.if

%changelog
* Wed Aug 26 2026 Julio Storch <julio.storch@netknights.it> - 1.0-4
- Ensure /var/log/privacyidea is relabeled after policy installation
- Remove unnecessary httpd executable file context
- Clean up SELinux policy for RHEL 8, 9 and 10

* Fri Jun 19 2020 Julio Storch <julio.storch@netknights.it> - 1.0-1
- SELinux build release
