%define source_name privacyIDEA
%define name privacyidea
%define version %{getenv:PI_VERSION} 
%define unmangled_version %{version}
%define unmangled_version %{version}
%define release 1
Name:           %{name}
Version:        %{version}
Release:        1%{?dist}
Summary:        two-factor authentication system e.g. for OTP devices

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       Cornelius Kölbel <cornelius.koelbel@netknights.it>
BuildArch:      x86_64

BuildRequires: libxml2-devel, freetype-devel, python-devel, libxslt-devel, zlib-devel, openssl-devel, python-virtualenv, gcc

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

%build
rm -fr /opt/privacyidea
virtualenv /opt/privacyidea
source /opt/privacyidea/bin/activate
pip install --upgrade pip
pip install privacyidea==%{version}
pip install pymysql==0.7.2
pip install pymysql_sa
pip install jinja2==2.8.1
pip install Pillow==2.9.0
# No Auth Modules in the base package
rm -fr /opt/privacyidea/lib/python2.7/site-packages/authmodules
rm -fr /opt/privacyidea/lib/privacyidea/authmodules

%install
mkdir -p $RPM_BUILD_ROOT/opt/
cp -r /opt/privacyidea $RPM_BUILD_ROOT/opt/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/opt/privacyidea

%changelog

%include %{_topdir}/changelog-privacyidea.inc
