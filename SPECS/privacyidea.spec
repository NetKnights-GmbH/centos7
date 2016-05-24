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

BuildRequires: libxml2-devel, freetype-devel, python-devel, libxslt-devel, zlib-devel, openssl-devel

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
pip install privacyidea==%{version}
pip install pymysql
pip install pymysql_sa
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
* Tue May 24 2016 Corneluis Kölbel <cornelius.koelbel@netknights.it> 2.12
- Event Handler Framework #360
- local CA connector can enroll certificates
  for users. Users can download PKCS12 file. #383
- Add and edit users in LDAP resolvers #372
- Hardware Security Module support via PKCS11
- Time dependent policies #358

- Enhancements
- Policy for web UI enrollment wizard #402
- Realm dropdown box at login screen #400
- Apply user policy settings #390
- Improve QR Code for TOTP token enrollment #384
- Add documentation for enrollment wizard #381
- Improve pi-manage backup to use pymysql #375
- Use X-Forwarded-For HTTP header as client IP #356
- Add meta-package privacyidea-mysql #376

- Fixes
- Adduser honors resolver setting in policy #403
- Add documentation for SPASS token #399
- Hide enrollment link (WebUI) is user can not enroll #398
- Fix getSerial for TOTP tokens #393
- Fix system config checkboxes #378
- Allow a realm to be remove from a token #363
- Improve the date handling in emails #352
- Sending test emails #350
- Authentication with active token not possible if
  the user has a disabled token #339

* Thu Feb 11 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.10
- User Registration: A user may register himself and thus create
  his new user account.
- Password Reset: Using a recovery token a user may issue a
  password reset without bothering the administrator or the help desk.
- Enrollment Wizard for easy user token enrollment
- SMTP Servers: Define several system wide SMTP settings and use
  these for Email token, SMTP SMS Provider, registration process,
  or password reset.

* Tue Jan 26 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.10dev5-1
- initial RPM packaging

