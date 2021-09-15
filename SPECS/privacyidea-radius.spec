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
Requires:       freeradius, freeradius-perl, freeradius-utils
Requires:       perl-URI-Encode
Requires:       perl-LWP-Protocol-https
Requires:       perl-Data-Dump
Requires:       perl-Config-IniFiles
Requires:       perl-JSON
Requires:       perl-Time-HiRes
Requires:       perl-Try-Tiny

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
# Install necessary files to BUILD_ROOT
install -D -m 755 %{build_dir}/git/privacyidea_radius.pm $RPM_BUILD_ROOT/usr/lib/privacyidea/privacyidea_radius.pm
install -D -m 644 %{build_dir}/git/rlm_perl.ini $RPM_BUILD_ROOT/%{_sysconfdir}/privacyidea/rlm_perl.ini
install -D -m 644 %{build_dir}/git/dictionary.netknights $RPM_BUILD_ROOT/%{_sysconfdir}/privacyidea/dictionary.netknights
install -D -m 640 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/sites-available/privacyidea
install -D -m 640 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-available/piperl
# Activate the piperl RADIUS module
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/mods-enabled
cd $RPM_BUILD_ROOT/etc/raddb/mods-enabled && ln -s ../mods-available/piperl .
# Activate the privacyidea RADIUS module
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/raddb/sites-enabled
cd $RPM_BUILD_ROOT/etc/raddb/sites-enabled && ln -s ../sites-available/privacyidea .

%post
# unlink not necessary modules
unlink /etc/raddb/mods-enabled/eap
unlink /etc/raddb/sites-enabled/default
unlink /etc/raddb/sites-enabled/inner-tunnel
# restart radius service
/bin/systemctl try-restart radiusd.service

%clean
rm -fr %{build_dir}/git
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

/usr/lib/privacyidea
%config(noreplace) /etc/privacyidea/rlm_perl.ini
%config(noreplace) /etc/privacyidea/dictionary.netknights
%attr(640,root,radiusd) %config(noreplace) /etc/raddb/sites-available/privacyidea
%attr(-,root,radiusd) %config(noreplace) /etc/raddb/sites-enabled/privacyidea
%attr(640,root,radiusd) %config(noreplace) /etc/raddb/mods-available/piperl
%attr(-,root,radiusd) %config(missingok) /etc/raddb/mods-enabled/piperl


%changelog

%include %{_topdir}/changelog-radius.inc
