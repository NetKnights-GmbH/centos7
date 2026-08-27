%global selinuxtype targeted
%global modulename privacyidea-pam-selinux
%global release 2

Name:           privacyidea-pam-selinux
Version:        1.0
Release:        %{release}%{?dist}
Summary:        SELinux policy for privacyIDEA PAM
License:        GPLv2
URL:            https://privacyidea.org
BuildArch:      noarch

Source0:        privacyidea-pam-selinux-src

BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel

# Runtime dependencies required by the SELinux RPM scriptlet macros.
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}

# Adds the appropriate SELinux userspace dependencies when the macro
# is available. Using ? keeps the SPEC compatible with future/older EL.
%{?selinux_requires}

%description
privacyidea-pam-selinux provides an SELinux policy module for
privacyIDEA PAM. It allows PAM consumers to communicate with a
privacyIDEA server and to access the privacyIDEA offline token data.

%prep
rm -rf %{_builddir}/%{name}-%{version}
cp -a %{SOURCE0} %{_builddir}/%{name}-%{version}

%build
cd %{_builddir}/%{name}-%{version}

make -f %{_datadir}/selinux/devel/Makefile \
    %{modulename}.pp

bzip2 -9 %{modulename}.pp

%pre
%selinux_relabel_pre -s %{selinuxtype}

%install
install -D -m 0644 \
    %{_builddir}/%{name}-%{version}/%{modulename}.pp.bz2 \
    %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%post
%selinux_modules_install \
    -s %{selinuxtype} \
    %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

# Apply file contexts from the newly installed policy immediately.
if [ -e /etc/privacyidea/pam.txt ]; then
    restorecon /etc/privacyidea/pam.txt >/dev/null 2>&1 || :
fi

%postun
if [ "$1" -eq 0 ]; then
    %selinux_modules_uninstall \
        -s %{selinuxtype} \
        %{modulename}
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}

%files
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%changelog
* Thu Aug 27 2026 Julio Storch <julio.storch@netknights.it> - 1.0-2
- Clean up SELinux policy packaging
- Support current Enterprise Linux releases
- Use standard SELinux policy packaging macros
- Remove unnecessary PAM library file context
- Remove privacyIDEA server log relabeling

* Tue Sep 26 2023 Julio Storch <julio.storch@netknights.it> - 1.0-1
- Initial SELinux PAM policy release
