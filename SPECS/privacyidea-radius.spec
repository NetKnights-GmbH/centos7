%define source_name privacyIDEA
%define name privacyidea-radius
%define version %{getenv:PI_VERSION}
%define unmangled_version %{version}
%define unmangled_version %{version}
%define source0  https://raw.githubusercontent.com/privacyidea/FreeRADIUS/master/privacyidea_radius.pm
%define source1 https://raw.githubusercontent.com/privacyidea/FreeRADIUS/master/rlm_perl.ini
%define source2 https://raw.githubusercontent.com/privacyidea/FreeRADIUS/master/dictionary.netknights
%define release 1
Name:           %{name}
Version:        %{version}
Release:        1%{?dist}
Summary:        privacyIDEA RADIUS plugin

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       Cornelius Kölbel <cornelius.koelbel@netknights.it>
BuildArch:      noarch

BuildRequires: libxml2-devel, freetype-devel, python-devel, libxslt-devel, zlib-devel, openssl-devel
Requires:      freeradius, freeradius-perl

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

%install
#rm -fr $RPM_BUILD_ROOT/usr/lib/privacyidea
mkdir -p $RPM_BUILD_ROOT/usr/lib/privacyidea
curl %{source0} -o $RPM_BUILD_ROOT/usr/lib/privacyidea/privacyidea_radius.pm
mkdir -p $RPM_BUILD_ROOT/etc/privacyidea
curl %{source1} -o $RPM_BUILD_ROOT/etc/privacyidea/rlm_perl.ini
curl %{source2} -o $RPM_BUILD_ROOT/etc/privacyidea/dictionary.netknights
mkdir -p $RPM_BUILD_ROOT/etc/raddb/sites-available/
cp $RPM_SOURCE_DIR/privacyidea-radius-site $RPM_BUILD_ROOT/etc/raddb/sites-available/privacyidea


%clean

%files
/usr/lib/privacyidea
/etc/privacyidea
/etc/raddb/sites-available/

%changelog
* Wed Apr 13 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.11-1
- Adding radius config

* Thu Feb 11 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.10
- packaging of release 2.10

* Thu Jan 27 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.10dev5-1
- initial RPM packaging

