* Fri Aug 27 2021 Netknights GmbH <release@netknights.it> 3.4.2
- Better logging
- Update privacyidea_radius.pm (#48)
- Add GitHub workflow file (#50)
- Fix failing perl versions and add GitHub workflow file (#53)
- Fix encoding issues with passwords (#54)
- Add link to docs

* Fri Jul 23 2021 Cornelius Kölbel <cornelius.koelbel@netknights.it> 3.4.1
- Fix the urlencoding of username and password to work
  with privacyIDEA 3.6. (#50)

* Mon May 25 2020 Cornelius Kölbel <cornelius.koelbel@netknights.it> 3.4
- Allow different configs with the same scriptto use redundant to
  ask different privacyIDEA servers. (#10)
- Add parameter ADD_EMPTY_PASS to handle RADIUS requests without User-Password.

* Wed Feb 26 2020 Cornelius Kölbel <cornelius.koelbel@netknights.it> 3.3
- Allow multiple same reply attributes

* Fri Aug 30 2019 Cornelius Kölbel <cornelius.koelbel@netknights.it> 3.2
- Remove default examples from rlm_perl.ini
- Fix a failure if config file is missing
- provide an extra perl module configuration, to avoid config clashes

* Thu May 23 2019 Cornelius Kölbel <cornelius.koelbel@netknights.it> 3.1
- Add timing to log file
- return RLM_MODULE_NOTFOUND in case the user is not found
- remove static user-dir mapping

* Tue Oct 11 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.15
- Add User Attribute Mapping

* Wed Apr 13 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.11-1
- Adding radius config

* Thu Feb 11 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.10
- packaging of release 2.10

* Wed Jan 27 2016 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.10dev5-1
- initial RPM packaging

