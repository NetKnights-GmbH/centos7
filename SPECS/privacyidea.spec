%define source_name privacyIDEA
%define name privacyidea
%define version %{getenv:PI_VERSION}
%define unmangled_version %{version}
%define release 1
%undefine __brp_mangle_shebangs
# Somehow stripping the '.comment' section from the Pillow libraries breaks the strip-tool,
# so we skip stripping and byte-compile in the postinstall scripts, otherwise Pillow will fail.
%global __os_install_post %(echo '%{__os_install_post}' | sed -re 's!/usr/lib[^[:space:]]*/((brp-python-bytecompile)|(brp-strip-comment-note))[[:space:]].*$!!g')
# don't add build-ids since we copy some libs from default locations
%global _build_id_links none
%global _tmp_build_dir %{_tmppath}/build_%{name}-%{version}-%{release}

Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        two-factor authentication system e.g. for OTP devices

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       NetKnights GmbH <release@netknights.it>
ExclusiveArch:  x86_64
AutoReqProv:    no
%if 0%{?rhel} < 9
BuildRequires:  python3-virtualenv, git
%endif
BuildRequires:  git

%description
 privacyIDEA: identity, multifactor authentication, authorization.
 This package contains the python module for privacyIDEA. If you want
 to run it in a productive webserver you might want to install
 privacyidea-server.
 privacyIDEA is an open solution for strong two-factor authentication.
 privacyIDEA aims to not bind you to any decision of the authentication protocol
 or it does not dictate you where your user information should be stored.
 This is achieved by its totally modular architecture.
 privacyIDEA is not only open as far as its modular architecture is concerned.
 But privacyIDEA is completely licensed under the AGPLv3.


%prep
rm -fr /opt/privacyidea
rm -fr %{_tmp_build_dir}/privacyidea
mkdir -p %{_tmp_build_dir}
git clone --recurse-submodules --branch v%{version} --depth 1 https://github.com/privacyidea/privacyidea.git %{_tmp_build_dir}/privacyidea

%build
%if %{rhel} < 9
python3.9 -m venv /opt/privacyidea
%else
python3 -m venv /opt/privacyidea
%endif

source /opt/privacyidea/bin/activate
pip install --upgrade pip setuptools
pip install -r %{_tmp_build_dir}/privacyidea/requirements.txt
pip install %{_tmp_build_dir}/privacyidea/

%install
mkdir -p $RPM_BUILD_ROOT/opt
cp -r /opt/privacyidea $RPM_BUILD_ROOT/opt

%clean
rm -rf $RPM_BUILD_ROOT

%files
/opt/privacyidea

%changelog
%include %{_topdir}/changelog-privacyidea.inc
