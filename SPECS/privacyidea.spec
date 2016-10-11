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
pip install pymysql==0.6.6
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
* Tue Oct 11 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.15
  Features
  * Client Overview. Display the type of the requesting
    authenticating clients (#489)
  * Support for NitroKey OTP mode (admin client)

  Enhancements
  * Performance enhancements using Caching singletons for
    Config, Realm, Resolver and Policies
  * Allow configuration of the registration email text (#494)
  * Return SAML attributes only in case of successful
    authentication (#500)
  * Policy "reset_all_user_tokens" allow to reset all
    failcounters on successful authentication (#471)
  * Client rewrite mapping also checks for
    X-Forwarded-For (#395, #495)

  Fixes
  * Fixing RemoteUser fails to display WebUI (#499)
  * String comparison in HOSTS resolver (#484)


* Wed Aug 24 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.14
  Features
  * Import PGP encrypted seed files
  * Allow UserNotification for user actions
  * Allow UserNotification on validate/check events,
    to notify the user on a failed authentication or
    a locked token.

  Enhancements
  * Add thread ID in REST API Response
  * Performance improvement: Cache LDAP Requests #473
  * Performance improvement: Optimize resolver iteration #474
  * Add "Check OTP only" in WebUI
  * Improve "get serial by OTP" in WebUI
  * Add script to get serial by OTP

  Fixes
  * Restrict GET /user for corresponding admins #460

* Thu Jun 30 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.13
- Features
- Allow central definition of SMS gateways
  to be used with tokens. #392
- User SMS for User Notificaton Event Handler. #435
- Add PIN change setting for each token. #429
- Force PIN change in web UI. #432

- Enhancements
- Performence enhancements
  speed up loading of audit log in web UI.
  avoid double loadin of tokens and audit entries in web UI. #436
- Additional log level (enhanced Debug) to even log passwords in
  debug mode.
- Add new logo. #430
- Add quick actions in the token list: reset failcounter,
  toggle active. #426
- REST API returns OTP length on successful authentication. #407
- Add intelligent OverrideAuthorizationClient system setting,
  that allows defined proxies to reset the client IP. #395

- Fixes
- Display token count in web UI. #437
- Use correct default_tokentype in token enrollment. #427
- Fix HOTP resync problems. #412


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

