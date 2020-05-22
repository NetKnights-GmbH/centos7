%define source_name privacyIDEA
%define name privacyidea-radius
%define version %{getenv:PI_VERSION}
%define unmangled_version %{version}
%define gitsource https://github.com/privacyidea/FreeRADIUS.git
%define release 1
%global build_dir %{_tmppath}/build_%{name}-%{version}

Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        privacyIDEA RADIUS plugin

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       Cornelius Kölbel <cornelius.koelbel@netknights.it>
BuildArch:      noarch

BuildRequires:  git
Requires:       freeradius, freeradius-perl, perl-LWP-Protocol-https, freeradius-utils
#Requires:       epel-release
#Requires:       perl-Data-Dump
#Requires:       perl-Config-IniFiles
#Requires:       perl-JSON
#Requires:       perl-Time-HiRes

Source1: privacyidea-radius-site
Source2: privacyidea-mods-perl

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
mkdir -p %{build_dir}/git
git clone %{gitsource} %{build_dir}/git
cd %{build_dir}/git; git checkout v%{version}
mkdir -p $RPM_BUILD_ROOT/usr/lib/privacyidea
install %{build_dir}/git/privacyidea_radius.pm $RPM_BUILD_ROOT/usr/lib/privacyidea/
mkdir -p $RPM_BUILD_ROOT/etc/privacyidea
install %{build_dir}/git/rlm_perl.ini $RPM_BUILD_ROOT/etc/privacyidea/
install %{build_dir}/git/dictionary.netknights $RPM_BUILD_ROOT/etc/privacyidea/
mkdir -p $RPM_BUILD_ROOT/etc/raddb/sites-available/
mkdir -p $RPM_BUILD_ROOT/etc/raddb/mods-available/
install %{SOURCE1} $RPM_BUILD_ROOT/etc/raddb/sites-available/privacyidea
install %{SOURCE2} $RPM_BUILD_ROOT/etc/raddb/mods-available/piperl

%post
# Activate the piperl RADIUS module
cd /etc/raddb/mods-enabled/
ln -s ../mods-available/piperl .
systemctl restart radiusd

%clean
rm -fr %{build_dir}/git
rm -rf $RPM_BUILD_ROOT

%files
/usr/lib/privacyidea
%config /etc/privacyidea
%config /etc/raddb/sites-available/*
%config /etc/raddb/mods-available/*


%changelog

%include %{_topdir}/changelog-radius.inc
