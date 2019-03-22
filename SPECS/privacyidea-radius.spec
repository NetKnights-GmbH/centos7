%define source_name privacyIDEA
%define name privacyidea-radius
%define version %{getenv:PI_VERSION}
%define unmangled_version %{version}
%define unmangled_version %{version}
%define gitsource https://github.com/privacyidea/FreeRADIUS.git
%define release 1
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        privacyIDEA RADIUS plugin

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       Cornelius Kölbel <cornelius.koelbel@netknights.it>
BuildArch:      noarch

BuildRequires: libxml2-devel, freetype-devel, libxslt-devel, zlib-devel, openssl-devel
Requires:      freeradius, freeradius-perl


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

%install
# Create git repo
mkdir -p $RPM_BUILD_ROOT/git
git clone %{gitsource} $RPM_BUILD_ROOT/git
cd $RPM_BUILD_ROOT/git; git checkout v%{version}
mkdir -p $RPM_BUILD_ROOT/usr/lib/privacyidea
cp $RPM_BUILD_ROOT/git/privacyidea_radius.pm $RPM_BUILD_ROOT/usr/lib/privacyidea/privacyidea_radius.pm
mkdir -p $RPM_BUILD_ROOT/etc/privacyidea
cp $RPM_BUILD_ROOT/git/rlm_perl.ini $RPM_BUILD_ROOT/etc/privacyidea/rlm_perl.ini
cp $RPM_BUILD_ROOT/git/dictionary.netknights $RPM_BUILD_ROOT/etc/privacyidea/dictionary.netknights
mkdir -p $RPM_BUILD_ROOT/etc/raddb/sites-available/
cp $RPM_SOURCE_DIR/privacyidea-radius-site $RPM_BUILD_ROOT/etc/raddb/sites-available/privacyidea
rm $RPM_BUILD_ROOT/git -fr


%clean

%files
/usr/lib/privacyidea
%config /etc/privacyidea
%config /etc/raddb/sites-available/*

%changelog

%include %{_topdir}/changelog-radius.inc
