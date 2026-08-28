%global selinuxtype targeted
%global modulename privacyidea-selinux
%global release 4

Name:           privacyidea-selinux
Version:        1.0
Release:        %{release}%{?dist}
License:        GPLv2
Summary:        SELinux policy for privacyIDEA
BuildArch:      noarch
URL:            https://privacyidea.org

Requires(post): selinux-policy-base
Requires(post): selinux-policy-targeted
Requires(post): policycoreutils
Requires(post): libselinux-utils

BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel

Source1:        privacyidea-selinux-src

%description
SELinux policy for privacyIDEA allowing the web server
to communicate with LDAP and database services and providing
the required file contexts for privacyIDEA log files.

%prep
rm -rf %{_builddir}/%{name}-%{version}
cp -r %{SOURCE1} %{_builddir}/%{name}-%{version}

%build
cd %{_builddir}/%{name}-%{version}

# Build the SELinux policy module using the distribution-provided
# SELinux development Makefile.
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp

# SELinux policy packages are installed compressed.
bzip2 -f %{modulename}.pp

%install
# Install the compiled SELinux policy module.
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}

install -m 0644 %{_builddir}/%{name}-%{version}/%{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/

%pre
# Save the current file-context configuration before installing
# the new SELinux policy.
%selinux_relabel_pre -s %{selinuxtype}

%post
# Install and load the privacyIDEA SELinux policy module.
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

# Apply the file contexts provided by the policy immediately.
# This is especially important for existing privacyIDEA log directories
# and files that may have been created with another SELinux context.
if [ -d /var/log/privacyidea ]; then
    restorecon -R /var/log/privacyidea >/dev/null 2>&1 || :
fi

%postun
# Remove the SELinux policy module only when the package itself
# is removed, not during an upgrade.
if [ "$1" -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans
# Relabel files whose expected contexts changed as part of this
# policy installation or upgrade.
%selinux_relabel_post -s %{selinuxtype}

%files
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%changelog
* Fri Aug 28 2026 NetKnights GmbH <info@netknights.it> - 1.0-4
- Modernize SELinux policy packaging for RHEL 8, 9 and 10
- Build policy using the distribution SELinux development Makefile
- Remove unused interface file and policy declarations
- Improve privacyIDEA log file context handling

* Fri Jun 19 2020 Julio Storch <info@netknights.it> - 1.0-1
- SELinux build release
