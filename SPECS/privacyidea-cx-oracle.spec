%define source_name cx_Oracle
%define name privacyidea-cx-oracle
#%define version 6.0rc1
%define version 6.3.1
%define unmangled_version %{version}
%define unmangled_version %{version}
%define release 1
Name:           %{name}
Version:        %{version}
Release:        1%{?dist}
Summary:        cx_Oracle python module for privacyIDEA

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       Cornelius Kölbel <cornelius.koelbel@netknights.it>
BuildArch:      x86_64

BuildRequires: libxml2-devel, freetype-devel, python-devel, libxslt-devel, zlib-devel, openssl-devel
Requires:      privacyidea

#Source0:       %{source0}

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
pip install cx_Oracle==%{version}

%install
mkdir -p $RPM_BUILD_ROOT/opt/privacyidea/lib/python2.7/site-packages/
cp -r /opt/privacyidea/lib/python2.7/site-packages/cx_Oracle* $RPM_BUILD_ROOT/opt/privacyidea/lib/python2.7/site-packages/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/opt/privacyidea/lib/python2.7/site-packages/cx_Oracle.so
#/opt/privacyidea/lib/python2.7/site-packages/cx_Oracle-%{version}-py2.7.egg-info
/opt/privacyidea/lib/python2.7/site-packages/cx_Oracle-%{version}.dist-info

%changelog
%include %{_topdir}/changelog-privacyidea.inc
