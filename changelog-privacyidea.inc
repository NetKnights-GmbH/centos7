* Fri Oct 08 2021 NetKnights GmbH <release@netknights.it> 3.7dev2

    Enhancements:
     * Support SMTPS (#2568)
     * Add policy extended conditions of webserver environment (#2510)

    Fixes:
     * Do not use not-readily enrolled tokens for auth  (#2852)
     * Allow tokens in client_wait to be rolled over (#2763)

* Fri Aug 27 2021 NetKnights GmbH <release@netknights.it> 3.7dev1

    Features:
    Enhancements:
     * Allow resyncing of a token via Multi-Challenge (#2349)
     * Token Handler can use the serial numbers of the tokens
       during token import (#2698)
     * Notification Handler now allows placeholders like "tokenowner" in reply-to. (#2711)
     * LinOTP miration script now also works with PostgreSQL (#2770)
     * consolidate client_wait in token enrollment. All tokens now
       get the rollout_state "clientwait" or "enrolled" which can
       be used in Token Handlers and in the token-janitor (#2784)
     * The "orphaned" parameter of the token-janitor allows to use
       0/False or 1/True to also search for non-orphaned tokens (#2838)
     * Add more export/import functions to pi-manage (#2455)

    Fixes:
     * Make token-janitor robust against unknown chars in last_auth check (#2780)
     * Fix the manual setting of U2F tokens, which was overwritten by an
       automatic description (#2793)
     * Improve parameter parsing and decoding (#2810)
     * Fix policy import with missing "condition" keyword (#2829)
     * Add failsafe to raise an exception on the lib level when trying to assign a token
       to a user, if the token is already assigned. (#2860)
     * Fix AD little endian in objectGUID
     * Fix upper case realm names in policy check (#2869)
     * Fix deleting expired auth_cache entries (#2481)

* Thu Jul 22 2021 NetKnights GmbH <release@netknights.it> 3.6.2

    Features:
    * Add custom user attributes that can be managed within privacyIDEA #680
    * Extended policy conditions can match on any token attribute #2590

* Mon Jul 19 2021 NetKnights GmbH <release@netknights.it> 3.6.1

    Fixes:
     * Remove importlib-metadata from doc requirements
     * Add a safe_store feature #2794
     * Decode URL parameters for forms #2800
     * Prepare ADFS subscription #2801

* Wed Mar 24 2021 NetKnights GmbH <release@netknights.it> 3.5.2

    Fixes:
     * Add serial to the request object in /ttype/ endpoint (#2605)
     * Fix missing audit entries missing_line and sig_check (#2627)
     * Fix backup on Ubuntu 20.04 (#2646)
     * Fix missing priority in policy import (#2643)
     * Fix DB migrate URI if it contains char % (#2661)
     * Fix long default POOLING_LOOP_TIMEOUT (#2662)
     * Fix tokeninfo value filter with Oracle db (#2602)
    
* Thu Jan 28 2021 NetKnights GmbH <release@netknights.it> 3.5.1

    Fixes:
     * Fix DB migration script for update from prior of 3.3. (#2582)
     * Fix the internal interface of container audit module (#2562)
     * Add missing headers to /auth request (#2599)
     * Fix tokeninfo value filter with Oracle db (#2602)

* Tue Dec 22 2020 NetKnights GmbH <release@netknights.it> 3.5
    
    Features:
     * 4Eyes token uses multi challenge authentication (#2317)
     * Require attestation certificate when enrolling
       certificate token (#2152)

    Enhancements:
     * Tokens
     * Allow to update firebase_token of a Push Token (#2436)
     * Support WebAuthn tokens without sign_count (#2361)
     * PSKC import now verifies the MAC of the token secrets (#2312)
     * Configure length and contents of registration token via policy (#2284)
     * The questionnaire token can now ask several questions from the list (#2137)
     * Event handler:
     * Choose SMS Gateway Identifier in Tokenhandler
       when enrolling SMS token (#2506)
     * Choose SMTP Identifier in Tokenhandler
       when enrolling Email token (#2452)
     * Increase or decrease failcounter in Tokenhandler (#2402)
     * Allow to set maxfail counter in event handlers (#2541)
     * Policies:
     * Add extended conditions for tokeninfo (#1947)
     * Web UI
     * PIN can be changed with Challlenge Response when authenticating
       at the WebUI (#2474)
     * Hide some audit log columns for service desk users (#2372)
     * Allow to configure a link to a policy statement/GDPR (#2325)
     * Audit log now contains start time, end time and
       duration of a request (#2254)
     * The length of the audit columns to be truncated can be
       configured in pi.cfg (#1756)
     * Action grouping in scope authorization (#2438)
     * Redesign welcome message for community version (#2397)
     * Add usernames and serials of failed authentications
       as shortlink into dashboard (#2475)
     * Policy to add node name in the web UI (#1961)
     * Make event conditions searchable (#2148)
     * Align search layout in event conditions and policy actions (#2557)
     * pi-manage: export resolver configuration (#1329)
     * Documentation:
     * Add note about SELinux and using non-standard ports (#2459)
     * Explain sync_to_database for script handlers (#2450)
     * Add documentation for RADIUS configuration (#2448)

   Fixes:
    * Allow equal signs in policy actions (#2494)
    * Challenge Response is now checked independently on the presence
      of a challenge in the database (#2491)
    * Fix enrollment of two tokens using double click (#2487)
    * Fix wrong (to few) number of authentication requests
      in the dashboard (#2473)
    * Allow setting an empty PIN in the UI (#2472)
    * The dashboard only displays information, which an admin is
      allowed to see, without throwing errors (#2456)
    * Fix length of hashed password column in auth_cache table (#2446)
    * Fix url_decode (#2345)
    * Fix missing adminuser when importing policies (#2340)
    * Hide browser autocomplete in user search field (#2292)



* Fri Oct 09 2020 NetKnights GmbH <release@netknights.it> 3.4.1

    Fixes:
     * Fix the deletion of the registration token (#2356)
     * Add "messages" to JSON response in case of multi challenge
       pin change (2346)
     * Move from PBKDF2 to Argon2 for password hashes. Might want to
       reset local admin passwords to use new hashing algo (#2412)
     * Hide dashboard for normal users (#2384)
     * Fix problem with missing templates in CA conncetor (#2374)
     * Fix missing successful authentications in dashboard (#2394)
     * Improve error handling in token janitor in case of
       problematic user (#2405)
     * remove PI_PEPPER and pyCrypto (#2409)
     * only check for existing JWT algorithms (#2407)
     * Use Argon2 for PINs and local admins (#2413)
     * Fix error when logging in with REMOTE_USER (#2423)
     * Use a secure way to compare strings to avoid
       theoretical side channel attacks (#2415)


* Wed Oct 07 2020 NetKnights GmbH <release@netknights.it> 3.4.1dev3

    Features:
     * Add ScriptSMSProvider, that can send SMS through external
       Gateways using arbitrary scripts (#2236)
     * Add HTTP Resolver that can read users from web services
       via JSON responses (#2083)
     * Add a basic dashboard as start screen in the WebUI (#2177)
     * Allow using dynamic 3rd party token classes (#2321)
     * Allow multiple consecutive challenge responses for authentication
       or tasks like changing the token PIN (#2361)
     * PUSH token can communicate with privacyIDEA via polling
       as fallback to Google Push Service or Apple Notification Service (#2262)

    Enhancements:
     * Allow deletion of validity period via UI (#2263)
     * Remove marker for missing translations and allow to set a
       custom marker (#2223)
     * Add support for Python 3.8 (#2190)
     * Allow hiding description field for users during
       token enrollment (#2173)
     * Improve error message during token import (#2073)
     * Add Dutch translation (#2314)
     * Allow application to choose tokentypes in
       /validate/check and /validate/triggerchallenge (#2047)
     * HTTPSMSProvider can now have header parameters in the
       provider definition (#1963)
     * Events
     * Add failcounter as condition in event handlers (#2147)
     * The script handler allows to sync the database before
       running the script (#2293 #2302)
     * Allow using user_obj in pre event handlers for
       /auth event. (#2303)
     * Policies
     * Allow to define characters for set_random_pin policy (#2121)
     * Add privacyIDEA nodes to policy condition (#2108)
     * Add new authz policy action is_authorized to basically
       allow or deny access (#2275)
     * Allow ECDSA and other SSH key types (#2274)
     * pi-manage can import tokens including HOTP token counter (#2285)
     * Allow the token janitor to set tokenrealms (#2299)
     * Use our general webauthn client component in the
       privacyIDEA WebUI (#2273)

    Fixes:
     * Add missing audit data to container audit (#2264)
     * Add tokeninfo failsafe for LinOTP migration script (#2253)
     * Fix certain problems with the type of the userid
       in SQL-Resolvers with Oracle DB (#2219)
     * Fix default empty string problems with Oracle DB (#2218)
     * Fix a policy issue that would require admin policies to
       import tokens (#2209)
     * Fix inconsistent enrollment templates. Have description
       field for all tokentypes (#2208)
     * Fix floating problems with multiple QR images in enrollment UI (#2175)
     * Allow to edit realms without resolver priority (#2171)
     * Fix empty (None) values in SQL Resolver connect string (#2271)
     * Fix missing options parameter in RADIUS and REMOTE token (#2276)
     * Use UTC for challenge timestamp (#1586)
     * Fix exceeding max tokens when enabling a disabled token (#2215)
     * split@Sign setting is also applied to REMOTE_USER (#1954)
     * Fix privacyidea-diag and privacyidea-standalone to run with Python 3 (#1874)
     * Fix possible recursion error in 4eyes token (#1892)
     * Improve tests by fixing deprecation warnings (#2298)
     * Clean up the code for /validate/samlcheck
     * Fix censoring of Oracle connect strings (#2304)
     * Treat unsupported WebAuthn attestation as None attestation (#2342)
     * Fix admin/scope in import/export of policies with pi-manage (#2359)
     * Fix url_decode (#2360)
     * Fix token settings for Yubikey in UI enrollment (#2365, #2366)


* Fri Sep 11 2020 NetKnights GmbH <release@netknights.it> 3.4

  Features:
   * Add ScriptSMSProvider, that can send SMS through external
     Gateways using arbitrary scripts (#2236)
   * Add HTTP Resolver that can read users from web services
     via JSON responses (#2083)
   * Add a basic dashboard as start screen in the WebUI (#2177)
   * Allow using dynamic 3rd party token classes (#2321)
   * Allow multiple consecutive challenge responses for authentication
     or tasks like changing the token PIN (#2361)
   * PUSH token can communicate with privacyIDEA via polling
     as fallback to Google Push Service or Apple Notification Service (#2262)

  Enhancements:
   * Allow deletion of validity period via UI (#2263)
   * Remove marker for missing translations and allow to set a
     custom marker (#2223)
   * Add support for Python 3.8 (#2190)
   * Allow hiding description field for users during
     token enrollment (#2173)
   * Improve error message during token import (#2073)
   * Add Dutch translation (#2314)
   * Allow application to choose tokentypes in
     /validate/check and /validate/triggerchallenge (#2047)
   * HTTPSMSProvider can now have header parameters in the
     provider definition (#1963)
   * Events
     * Add failcounter as condition in event handlers (#2147)
     * The script handler allows to sync the database before
       running the script (#2293 #2302)
     * Allow using user_obj in pre event handlers for
       /auth event. (#2303)
   * Policies
     * Allow to define characters for set_random_pin policy (#2121)
     * Add privacyIDEA nodes to policy condition (#2108)
     * Add new authz policy action is_authorized to basically
       allow or deny access (#2275)
   * Allow ECDSA and other SSH key types (#2274)
   * pi-manage can import tokens including HOTP token counter (#2285)
   * Allow the token janitor to set tokenrealms (#2299)
   * Use our general webauthn client component in the
     privacyIDEA WebUI (#2273)

  Fixes:
   * Add missing audit data to container audit (#2264)
   * Add tokeninfo failsafe for LinOTP migration script (#2253)
   * Fix certain problems with the type of the userid
     in SQL-Resolvers with Oracle DB (#2219)
   * Fix default empty string problems with Oracle DB (#2218)
   * Fix a policy issue that would require admin policies to
     import tokens (#2209)
   * Fix inconsistent enrollment templates. Have description
     field for all tokentypes (#2208)
   * Fix floating problems with multiple QR images in enrollment UI (#2175)
   * Allow to edit realms without resolver priority (#2171)
   * Fix empty (None) values in SQL Resolver connect string (#2271)
   * Fix missing options parameter in RADIUS and REMOTE token (#2276)
   * Use UTC for challenge timestamp (#1586)
   * Fix exceeding max tokens when enabling a disabled token (#2215)
   * split@Sign setting is also applied to REMOTE_USER (#1954)
   * Fix privacyidea-diag and privacyidea-standalone to run with Python 3 (#1874)
   * Fix possible recursion error in 4eyes token (#1892)
   * Improve tests by fixing deprecation warnings (#2298)
   * Clean up the code for /validate/samlcheck
   * Fix censoring of Oracle connect strings (#2304)
   * Treat unsupported WebAuthn attestation as None attestation (#2342)
   * Fix admin/scope in import/export of policies with pi-manage (#2359)
   * Fix url_decode (#2360)
   * Fix token settings for Yubikey in UI enrollment (#2365, #2366)

* Tue May 19 2020 NetKnights GmbH <release@netknights.it> 3.3.3

  Fixes:
    * Fix failing Challenge Response in WebUI (#2192)
    * Add better logging for contradciting policy calls
    * Case insensitive user check failsafe in policy matching (#2198)

* Wed May 06 2020 NetKnights GmbH <release@netknights.it> 3.3.2

  Fixes:
    * Fix restricted audit log for helpdesk users (#2181)

* Wed Apr 29 2020 NetKnights GmbH <release@netknights.it> 3.3.1
  
  Fixes:
    * Fix broken U2F support (#2157)
    * Fix creation of PGP keys with pi-maange (#2165)

* Sun Apr 05 2020 NetKnights GmbH <release@netknights.it> 3.3

  Features:
    * New token type: WebAuthn/FIDO2 token is initially supported by privacyIDEA (#1468)
    * New token type: Indexed Secret token allows user
      to authenticate with a pre-known secret that can be
      initialized from the user store. (#1986)
    * New Event Handler Module: Logging module enables custom event-driven logging (#1580)

  Enhancements:
    * Event Handler:
      * The OTP token QR code can now be added not only inline but also as an attachment
        to email notifications (#1226)
    * Policies:
      * Added a policy to define the allowed characters for PINs (#2051)
      * Add policies to limit the number of destinct tokentypes per user (#1375)
      * Improved distinction between the username of the administrator
        and the username of the user. Add an admin username to policies. (#1867)
        Thus allowing:
        * User attribute conditions in admin policies
        * default settings for hashlib and otplen for HOTP and TOTP token
         and default timestep for TOTP token can now be dependent on
         admin user and for which user the admin does the enrollment
        * Enrollment settings for push tokens can distinguish better
         between admin users and user
        * Random PIN settings can be user dependent
    * WebUI
      * Added the option to filter tokens by tokenrealm (#545)
      * Prior to enrollment of soft tokens, such as HOTP, TOTP and PUSH the user is
        offered with a QR codes to direct him to the Authenticator App stores (#1919).
      * Adding version hashes to WebUI components to avoid working with outdated
        templates (#1871)
      * Updated bootstrap and AngularJS (#830)
      * Rework policy matching (#1691 #2024 #2038)
    * Documentation
      * The documentation was restructured and updated (#1967 #1981 #1504 #2049 #2089 #2090).
    * Tools
      * Added a migration script to update the database schema from 2.23.5 to 3.2.2 (#2040)
    * Misc
      * Added the remote serial to the tokeninfo of a remote token to better track
        authenticated devices (#2031)
      * Use dictConfig instead of fileConfig to read configurations (#2059)
      * Support logging configuration file in YAML format (#2080)
      * Support custom audit logger names (#2106)

  Fixes:
    * Fix unauthorized statistics view (#1238)
    * Fix a bug which caused an exception during PSKC key file container import (#1915)
    * Fix link on privacyIDEA logo in the WebUI when no user is logged in (#1944)
    * Updated CA files in testdata which were about to expire (#1960)
    * Fix API endpoints to avoid redirects (#1999)
    * Fix url_decode padding before it could cause any issues (#2000)
    * Initialize rtype in user_object correctly (#2007)
    * Fix an inconsistency of start_tls with postgres SQL (#2025)
    * Fix wrong type splitting of questionnaire token (#2026)
    * Fix a bug which could cause missing audit entries when using the
      ContainerAudit module (#2029)
    * Fix a bug which prevented defining an SQL resolver without a password (#2030)
    * Fix missing "position" argument on event import with pi-manage (#2036)
    * Fix timing issues in tests (#2041)
    * Fix documentation (#2049)
    * Fix sorting token table by column (#2111)

* Fri Jan 17 2020 NetKnights GmbH <release@netknights.it> 3.2.2

  Fixes:
  * Fix Popen calls like with pi-manage backup restore
  * Fix retrieving the correct database for restore
  * Fix caconnectorread policy

* Tue Dec 31 2019 NetKnights GmbH <release@netknights.it> 3.2.1

  Fixes:
  * Fix the wording and translation of the lost token scenario

* Mon Dec 02 2019 NetKnights GmbH <release@netknights.it> 3.2

  Features:
  * New Event Handler: RequestMangler to modify request attributes (#1810)
  * New Event Handler: ResponseMangler to modify the response data (#1138)
  * New Audit Module to write to a file (#1072)
  * New Container Audit Module to write to several audit modules at once (#1072)
  * Applications can use the API with predefined asymmetric JWT (#1773)

  Enhancements:
  * Authentication:
    * Add endpoint /validate/polltransaction for an improved workflow
      for out-of-band challenges-responses like PUSH token (#1838)
    * Allow registration token to work as challenge/response (#1897)
    * RADIUS token also uses timeout and retries (#1931)
    * Improve the handling of splitAtSign, so that a multi-realm
      setup will be more consistent (#1808)
    * Use authentication and authorization policies also for the
      /auth endpoint (#1722, #1537)
  * Policies and events:
    * Allow HTTP AGENT and any arbitrary HTTP header in extended policy conditions (#1425)
    * Allow HTTP AGENT as condition for event handlers (#1260)
    * Event Handlers can match for the rollout_state (#1801)
    * Add write-to-file action to the notification handler (#717)
    * Allow user endpoints to trigger events (#1822)
  * Management:
    * Allow help desk to trigger a token PIN reset without actually seeing the PIN (#1196)
    * Allow "file:" syntax in email notification handler (#1939)
    * Allow more sophisticated Proxy settings for the OverrideClient settings (#1868)
    * LinOTP migration script to work with LDAP mixed endian notation (#1883)
    * triggerchallenge also writes the serial of the triggered token
      to the audit log (#1862)
    * Allow a dash ("-") in policy names (#1813)
    * The token janitor can return a list of users with tokens (#1705)
    * Restrict OTP length, hash and timestep also in admin policies (#1566)
  * User experience:
    * Clean up event handler view and put handler and
      position in extra columns (#1920)
    * Improve the serial number checking for disallowed characters (#1826)
    * The event handler list can be sorted and filtered (#1818)
    * The policy list can be sorted and filtered (#1817)
    * Show disallowed policy name characters in the UI (#1674)
    * Ask before deleting a hardware token (#954)
  * Performance:
    * Improve performance by reading event handlers only if the
      configuration has changed (#1823)
    * Store statistics data like event counters per node to improve
      HA and replication performance (#1819)
    * Improve performance of the pre-auth event handler (#1686)

  Fixes:
  * Delete entries from database tables, when the parent object
    is deleted (fixed for machineresolverconfig, resolverconfig,
    eventhandleroption) (#1927)
  * Comply to new pyredis parameters for apache auth module (#1925)
  * Fix filename parameter of HostMachineResolver (#1912)
  * Fix JSON content detection for endpoints like /validate/radiuscheck (#1850)
  * Fix integer UID with PostgreSQL databases (#1825)
  * Make the policy creation at the command line with pi-manage more
    consistent (#1807)

* Fri Nov 15 2019 NetKnights GmbH <release@netknights.it> 3.1.2

  Fixes:
  * Fix the missing phone number field for SMS token, when a user
    wants to enroll an SMS token. (#1929)

* Wed Sep 25 2019 NetKnights GmbH <release@netknights.it> 3.1.1  

  Fixes:
  * Fix the wrong token_type key in the audit log which caused the tokentype
    to not be contained in the audit (#1846)

* Wed Sep 04 2019 NetKnights GmbH <release@netknights.it> 3.1

  Features:
  * Allow user attributes in policy conditions (#1645)
  * Assign tokens and set old PIN during migration (#1619)
  * Admins can only see tokens within the realm they are allowed to manage (#1713)
    **Note**: During update a policy "pi-update-policy-b9131d0686eb" is added, which
    gives admins the previous read rights on tokens.
  * Add adminread policies for policies, events, resolvers, system, machineresolvers,
    smtpserver, radiusserver, privacyidea server, periodic tasks, smsgateways. (#1495)
    **Note**: During update a policy "pi-update-policy-3d7f8b29cbb1" is added, which
    gives read rights to all admins to provide backward compatibility

  Enhancements:
  * Authentication and Challenge Response:
    * RADIUS token supports a single AccessChallenge with the remote RADIUS server (#1790)
    * Improving Push token performance by reusing still valid access token (#1795)
    * Improving TiQR token: It returns the remaining attemps after a wrong PIN is given (#1777)
    * Improving TiQR token: Make TiQR info URL configurable (#1782)
    * Enhance validate check logic in regards to serials and user names (#1768)
    * User may now have several TiQR tokens at the same time (#1739)
    * Do not increase fail counter when *checking* for an answered challenge (#1697)
    * Allow additional token specific checks when answering challenge response (#1695)
    * Endpoint GET /token/challenges also takes transaction_id (#1689)
    * Push token can delay the response of /validate/check, so that there is no need 
      to query the server to check if the push notification has been answered (#1583)
  * User experience:
    * Improve user experience when enrolling Yubikeys via ykpersonalize - Automatically 
      removing whitespaces (#1735)
    * Allow user to change the token description (#1717)
    * Customize Web UI page title (#1624, #1243)
    * *search_on_enter* also applies to audit log (#1493)
    * Allow a welcome message in the Web UI if the user has no token (#1074)
    * Do not display token configuration hints in the UI to normal users (#1789)
  * Management:
    * Event handlers allow rollout_state as condition (#1801)
    * Add script to export OTP counters (#1728)
    * Allow many additional tags in email notifications: serial, user, givenname,
      surname, username, userrealm, tokentype, recipient_givenname, recipient_surname,
      time, date (#1703)
    * Improve diagnostics script by adding SQLAlchemy URL (#1667)
    * Add resolver conditions to several policy checks (#1646)
    * /auth entries in the audit log now also fill in resolver and serial (#1593)
    * `pi-manage backup` also backs up the FreeRADIUS configuration (#1575)
    * Allow event handlers on /auth endpoint (#1567)
    * Allow to force a PIN on tokens in the privacyIDEA Authenticator App (#1295)
    * New policy *max_active_tokens_per_user* (#1241)
    * Add image url to the otpauth QR code, allow images in e.g. FreeOTP (#1228)
    * Add MAC to PSKC token export (#1663)
  * Performance:
    * Make the serverpool in LDAP resolver persistant improving redundancy performance (#1396)

  Fixes:
  * Improve the stability of the schema-update-script (#1760)
  * Rearrange update order in migration scripts (#1733)
  * Adapt privacyidea-token-janitor to run with the TokenOwner table (#1709)
  * Reordering decorators and policy checks to avoid unnecessary error messages (#1751)
  * Fix user enrollment for tokens that require certain read rights for RADIUS and 
    certificates by adding additional endpoint /system/names/... (#1749, #1748)
  * Use same transaction ID for all user tokens even with a  TiQR token (#1723)
  * Improve challenge response to also check the matching of the transaction ID
    right at the beginning (#1699)
  * Add event API requests to Audit log (#1600)
  * Fix configuring pre-eventhandler with empty condition makes authentication fail (#1658) 
  * Improve UI by changing the cursor on all clickable elements (#1725)
  * Web UI: Focus the filter entry field in tables, when the filter is activated (#1661)
  * Fix some broken links in UI (#1610)
  * Fix double listing in policy list (#1132)
  * Remove additional empty line in audit log in case of an error (#1707)
  * Fix enrollment of certificate tokens under Python 3 (#1799)

* Mon Jun 17 2019 NetKnights GmbH <release@netknights.it> 3.0.2
  
  Fixes:
  * Fix creation of table tokenover and update with PostgreSQL DB
  * Fix user assignment migration with non-ascii characters in userid

* Thu May 23 2019 NetKnights GmbH <release@netknights.it> 3.0.1

  Fixes:
  * Fix PUSH token issues:
    * Add logic checking to setup of PUSH token (#1592)
    * Remove double enrollment notification of PUSH token in WebUI (#1598)
    * Fix to allow spaces in Firebase configuration (#1599)
    * Add support for iOS Firebase configuration (#1608)
    * Fix to allow PUSH token enrollment, even with Label-policy (#1589)
    * Fix to mark PUSH token challenge answered in the database (#1584)
  * Fix the validity period of the registration token (#1587)
  * Beautify the vertical alignment in the Web UI top menu (#1559)
  * Fix user cache configuration read - defaults to 0 (#1596)
  * Remove links in audit log for normal users (#1497)
  * Check UI rights for user resolvers (#1496)
  * Fix placeholder in realm dropdown in login dialog (#1498)
  * Fix enckey creation in Python 3 (#1594)
  * Allow the usage if "browserLanguage" in custom templates (#1620)
  * Open all accordions when searching for policy action (#1558)
  * Fix to hide support links also in menu (#1626)

* Thu Sep 06 2018 NetKnights GmbH <release@netknights.it> 2.23.1

  Features:
  * Add periodic tasks including a privacyidea-cron script. (#992) 
  * Add task module "Simple Stats" to generate time series of certain 
    important statistics values in privacyIDEA (#1105)
  * Add task module "Event Counter" that allows to create time series of 
    any arbitrary event. (#1029)
  * New token type: TAN list, that can also import a prefefined
    list of TANs (#1057)
  * Add Event Handler Pre-Handling, that e.g. allows for
    even more easy token enrollment concepts (#747)

  Enhancements:
  * Improve performance by adding SQL pooling for SQL Audit 
    and SQL Resolvers. (#1167, #1140)
  * Improve SQL Resolver to also verify bcrypt-hash passwords (#1172)
  * Allow multiple WHERE conditions in SQL Resolver (#1039)
  * Allow objectGUID as loginname in LDAP resolver for better 
    ownCloud support (#1076)
  * Add command in pi-manage to dump audit log information (#1120)
  * Add script to allow generation of AES keys on HSM (#1159)
  * Improve recovery mechanism from a lost HSM connection (#1069)
  * Improve Debug Logging to hide passwords in SQL connect strings (#1162)
  * Add script for easy privacyIDEA standalone setup (#1093)
  * ldap3, pyasn1, croniter updated in Ubuntu Launchpad repo (#1085)
  * Add a script that easily gathers support and diagnostic information (#829)
  * Add event handler management to pi-manage (#1119)
  * Allow to customize the challenge text for challenge response tokens (#1096)
  * Add user information to OATH CSV token import file (#998)
  * Improve migration scripts from LinOTP to also update counter values (#1075)
  * Add priority to policies to avoid contradicting policies (#1031)
  * The token event handler now can delete tokeninfo (#988)
  * Make the import of OATH CSV token specific, so that each 
    tokentype can define its own import strategy (#1066)
  * The Event Counter module now allows to decrease the counter (#991)
  * Allow time deltas to also contain seconds (#1033)

  Fixes:
  * Allow to use unicode passwords with non-ascii characters for the
    connect string in SQL Resolvers (#1181)
  * Fix problem that a wrong password hash was used, if user is created
    in SQL Resolver (#1114)
  * Fix performance issue with slow token listing (#1123)
  * Fix the QR code regeneration if the user already has the maximum number
    of allowed tokens (#1153)
  * Fix problem with privacyidea-pip-update in case of pip version 10 (#1128)
  * Fix problem if max_token_per_user was higher than 9 (#1117)
  * Fix hash algorithm in QR Code (#1088)
  * Set focus in username field in the login dialog (#205)
  * Fix disappearing scrollbar issue (#1020)
  * Fix import of SHA256 tokens (#1061)
  * Convert string values to unicode in the database model to 
    avoid misleading "error" messages (#1000)
  * Fix truncation of audit log in case of authentication failure (#1034)
  * Shorten audit information to fit into the database column (#1037)
  * Fix the RADIUS configuration test (#1042)
  * Fix PassOnNoUser in combination with event handler (#1206)
  * Fix loading of Event handler detail view (#1210)
  * Fix Challenge-Response login at Web UI (#1216)
  * Fix triggerchallenge to only use active tokens (#1217)
  * Write all installed package to diagnostics file and
    also write the resolver config in privacyidea-diag



* Tue Jul 31 2018 NetKnights GmbH <release@netknights.it> 2.22.4

  Fixes in Server:
  * Fix the get_token_type to no issue an SQL request for token searches
  * Optimize HSM aeshsm.py module

* Mon Jun 25 2018 NetKnights GmbH <release@netknights.it> 2.22.3


  Fixes in Server:
  * Fix the pskc export and import of pw token types (#1011)

* Tue May 29 2018 NetKnights GmbH <release@netknights.it> 2.22.2

  Fixes in WebUI:
  * Fix the missing scrollbar in all remaining cases.

  Fixes in Server:
  * Avoid cast problems with Oracle token DB when saving
    integer values to string columns.

* Fri Apr 20 2018 NetKnights GmbH <release@netknights.it> 2.22.1

  Fixes in WebUI:
  * Allow to display the messages of several C/R tokens (#995, #1004)
  * Use ng-if instead of ng-show to avoid errors in the javascript console (#963)
  * Remove reference to not-used system.addons.js to avoid errors in the javascript console
  * Remove reference to not-used system.addons.html to avoid errors in the javascript console
  * Use ng-src instead of src to avoid errors in the javascript console
  * Avoid request to /false is image is not existing - avoid error in the javascript console
  * Fix handling of U2F token in the WebUI login
  * Require serial number in the assignment form (#1011)
  * Fix PIN comparison in token enroll and token assign (#1010)
  * Fix the empty username in token enroll or assign (#918)

  Fixes in Server:
  * Add check for serial number present (#1011)
  * Fix validation of OCRA and TiQR token (#1008)
  * Add retry to cope with HSM issues (#1003)
  * Fix unicode in resolverconf database table with Oracle (#999)


* Tue Mar 27 2018 NetKnights GmbH <release@netknights.it> 2.22

  Features:
  * Add automatic offline refill for Offline OTP tokens (#839)
  * Return realm and resolver of the user and allow mapping
    group membership to the RADIUS protocol (#896)
  * Add new tokenkind (hardware, software, virtual) for all tokens (#828)
  * Support Vasco tokens via Import and via Web Enrollment (#904, #903, #891)
  * Add arbitrary tokeninfo field to authorization policy (#873)
  * New SMPP SMS provider (#878)
  * New event handler Counter for counting events for statistics and monitoring (#951)

  Enhancements:
  * Enhance the statistics possibilities in WebUI (#950)
  * Allow reencryption of the database by importing PSKC to
    a new database (#940)
  * Allow token janitor to export "PW" token type to PSKC (#942)
  * Also export and import the counter values of HOTP/TOTP to PSKC (#943)
  * SMS token can dynamically read phone number from user source (#932)
  * Email token can dynamically read email address from user source (#932)
  * Add policy to ignore the validity of a U2F attestation certificate (#926)
  * Improve the speed of the LinOTP migration script to cope with tens of
    thousands of tokens (#914)
  * pi-manage can create API tokens with a chosen validity time (#931)
  * Allow user to set token description for HOTP and TOTP tokens 
    during enrollment (#928) (Thanks to Taylor Chase for this contribution!)
  * Add timeout to SMTP server configuration (#919)
  * Allow complex email templates for email tokens (#684)
  * LDAP resolver now supports arbitrary multivalue attributes (#881)
  * Allow Event Handler to match failing authentication (#971)

  Fixes:
  * Several fixes in LDAP resolver to cope with ldap3/pyasn1 version issues and
    other issues (#911, #980, #982, #887)
  * Skip misguiding LDAP error "AttributeError NonType" in log file (#948)
  * Add missing validity time in /validate/check response for email tokens (#946)
    (Thanks to Kleber Rocha/klinux for this contribution!)
  * Fix the handling of the SMS expiration date (#937)
  * Fix serial length in the audit table to match the serial length in the token table (#929)
    (Thanks to Salvo Rapisarda for this contribution!)
  * Fix Mail content sent by email token is rendered as attachment (#915)
  * Fix Editing SMTP Server definition clears the password (#923)
  * Fix pi-manage backup crash (Thanks to Pavol Ipoth for this contribution!)


* Wed Jan 24 2018 NetKnights GmbH <release@netknights.it> 2.21.4

  Fixes:
  * HTTP Timeout of HTTP SMS Gateway (#889)
  * Remove console.log from webui


* Tue Jan 09 2018 NetKnights GmbH <release@netknights.it> 2.21.1 

  Fixes:
  * Allow to use TLS1.1 and TLS1.2 for LDAP Resolver (#876)

* Wed Dec 20 2017 NetKnights GmbH <release@netknights.it> 2.21

  Features:

   * Allow export of tokens to PKSC file (#790)
   * Implement two-step enrollment of HOTP/TOTP tokens (#797, #863, #865, #866)
   * Allow WebUI customization via policies (#795)

  Enhancements:

   * Add script to decrypt safeword tokens
   * Allow using tags in the tokenissuer of smartphone tokens
   * Try to re-establish lost HSM connections (#787)
   * Allow to rotate audit log based on multiple conditions (#780, #833)
   * Add dry-run option to audit log rotation (#801)
   * Allow dots in realm names (#808)
   * Mark empty but required fields in WebUI (#810)
   * Display success information after PIN is set (#822)
   * Add further tags to the user notification event handler (#824)
   * Add number of users to the subscription view (#800)
   * Add HTTP/HTTPS proxy settings to HTTP SMS Provider (#835)
   * Federation Handler allows to forward the authorization token (#838)
   * Use token janitor to export a user list (#852)
   * Use HSM for random key generation if possible (#783)
   * HTTP SMS Provider now takes TIMEOUT parameter into account
   * Allow to configure length of generated serial numbers (#583)

  Fixes:

   * Fix handling of only_realm option in token event handler (#809)
   * Fix scrollbar issues in WebUI (#806, #823)
   * Fix OTP counter of offline token (#840)
   * Fix conflicts between check_tokentype and passthru policies (#846)
   * Properly reset tab tile after session has been locked (#850)
   * Fix handling of fixed key size during enrollment (#820)
   * Make sure that only active policies are honored (#825)
   * Fix various bugs with non-ASCII data (#754)
   * Fix failcounter_clear_timeout (#831)
   * Only remove apache host definitions on first installation (#834)

* Mon Oct 30 2017 NetKnights GmbH <release@netknights.it> 2.20.1 

  Fixes:
   * /token/init allows to pass otpkey AND genkey=false (#793)
   * Cast date to string, to fix audit search for postgresql (#786)
   * Optimize the LDAP Resolver Redundancy to avoid LdapServerPoolExhaustedErrors (#802)
   * Preset default realm in token enrollment (#804)
   * Fix PassOnNoUser and PassOnNoToken (#798)
   * Fix genkey=0 error during token enrollment (#793)

* Wed Sep 27 2017 NetKnights GmbH <release@netknights.it> 2.20

  Features:

   * New Token-Type OCRA and DisplayTAN to support 
     transaction signing for online banking (#767)
   * Federation Handler allows to forward authentication
     requests and other REST API requests to a child
     privacyIDEA system (#711)
   * Improved Subscription Handling 
   * Allow to login with multiple loginnames (#713)
   * Authentication Cache policy (#729)

  Enhancements:

   * !!!NOTE!!! following policies now also honor the resolvers,
    which they did not previously:
    (AUTH, challenge_response), (AUTH, otppin), 
    (AUTHZ, auth_max_success), (AUTHZ, auth_max_fail),
    (AUTHZ, last_auth), (WEBUI, login_mode),
    (ENROLL,losttoken_pw_contents), (ENROLL,losttoken_validity),
    (ENROLL, losttoken_pw_len) (#736)
   * User can regenerate the QR Code during enrollment
     of smartphone app (#766)
   * Administrator can define remote privacyIDEA servers
     centrally (#711)
   * Events can now be ordered. This is important for the
     federation handling (#711)
   * Specify the hash algorithm that is used to save 
     SQL users passwords (#745)
   * Add welcome dialog for administrator (#716)
   * Allow creating oracle DB (#752)
   * Event Handler can use timestamps and time offsets in
     conditions (#741)
   * Use challenge/response token to unlock the screen of 
     the web UI (#702)
   * Support multiple challenge/response token at the same
     time (#722)
   * GPG keys are generated during package installation and
     show the GPG key in the import dialog (#742)
   * Failcounter clearing timeout in UI (#719)
   * Allow to send challenge data (like banking transaction) in
     email text and SMS text.

  Fixes:

   * Set default loglevel from DEBUG to INFO (#765)
   * Fixed PIN logging, which could lead to exceptions
   * Fixed unicode handling in log messages
   * Make LDAP Resolver work with utf8 (#738)
   * User can only choose hash algo according to policy (#723)
   * Add time period 30/60s to rollout URI (#744)
   * Fix deprecation warning for flask_migrate (#734)
   * Allow multiple tries for challenge/response (#708)
   * Fix problem with certificate serial number (#737)




* Sun Jul 02 2017 NetKnights GmbH <release@netknights.it> 2.19.1

  Version 2.19.1, 2017-07-02

  Enhancements:

  * Add "pi-manage policy load" and "pi-manage policy export". (#721)
  * Allow customization via pi.cfg file.
  * Add {username} and {realm} as tags for the tokenhandler. (#735)

 Fixes:

  * Fix pi-manage file permission for backup
  * Fix search for resolver in audit log
  * Allow to read old legacy time from validity period
  * Fix wrong enddate with lost_token
  * Fix typos
  * Improve documentation for yubikey
  * Improve documentation for cache decorator
  * Improve documentation for webui policy

  Version 2.19, 2017-05-25

  Features:
  * Add generic User Cache to speed up authentication (#670, #683)
  * Support multiple challenge-response tokens with the same PIN (#654)
  * Restrict U2F registration based on assertion certificte (#648)
  * Restrict authentication with U2F devices based on assertion 
    certificate (#648)
  * Add privacyidea-token-janitor script, that can clean orpaned or 
    expired tokens (#692)
  * Add API for mutual key generation during enrollment for easy 
    Smartphone App development by introducing a generic 
    2-step-rollout process (#627)
  * Add /validate/radiuscheck which works with rlm_rest and only uses 
    HTTP return codes. (#703)

  Enhancements:

  * Allow to unset token validity period and other tokeninfo
    fields (#691)
  * Add a quick-resolver test for LDAP resolvers (#688)
  * Add additional tokeninfo tags {client_ip}, {ua_browser}, 
    {ua_string} in token handler (#687)
  * Allow to set decription of U2F tokens during enrollment (#685)
  * Reduce the number of LDAP requests to increase authentication
    performance (#664, #655, #650)
  * Realm administrator is only allowed to see actions on this allowed
    user realms (#663)
  * Add audit rotation to pi-manage (#657)
  * Speed up Audit Log calls by adding a second index (#656)
  * Allow to either lock und logout the UI after timeout (#653)
  * Allow string format {user}, {realm}, {serial}, {surname} in 
    tokenlabel policy (#646)
  * Move to a consistent time format for validity period and all other 
    user specific times also containing the timezone (#644)
  * Add TLS certificate check to LDAP machine resolver (#638)
  * Make TLS certificate the default option in LDAP resolvers (#639)
  * Allow to use privacyIDEA ownCloud App without subscription
    file with up to 50 users.

  Fixes:
  * Fix the datepicker for the token validity period (#644 / #693)
  * Fix LDAP resolver to respect all boolean configuration 
    options (#658)
  * Fix serial number in challenge response validation response (#649)


* Tue Mar 28 2017 NetKnights GmbH <release@netknights.it> 2.18.1

  Features:
  * Allow to disable the WebUI (#605)
  * The WebUI will lock the screen after a timeout instead of  
    logging out the user. This allows to easily continue
    configuration work. (#621)
  * Improve the creation and handling of local CAs (#630, #632, #633)
    Allow certificate template for certificates with different runtime
    and x509v3 extensions.

  Enhancements
  Enhancements in Policies:
  * Allow regular expressions in usernames in policies. (#581)
  * Improve Policy creation with pi-manage from JSON formatted file.
  * WebUI: Add action grouping in policies.
  * WebUI: Add action filter in policy view.
  * Allow token specific PIN policies: The SPASS token can now
    have dedicated PIN policies.
  * Add PIN policies for administrators during enrollment and
    during assignment.
  * Add WebUI policy: only search on enter being pressed (#617)

  Enhancements in Event Handlers:
  * Add token_validity_period condition to event handlers. (#618)
  * Add additional options in token handler when creating 
    SMS, Email or mOTP tokens.
  * Allow tokenhandler to set tokeninfo field.
  * Allow tokenhandler to set syncwindow.
  * Add event handler condition for count_auth_success and
    cound_auth_fail
  * Add event handler condition for last_auth.
  * Improve Audit Log for Event Handler. Each triggered action 
    will now also create an audit entry. (#609)
  * Allow the use of {current_time} in tokenevent handler. (#628)

  Enhancements in LDAP Resolver:
  * Upgrade dependency to ldap3 version >=2.1.1 to improve LDAP 
    performance in regards to redundancy and security
  * LDAP Resolver: Use get_info in bind requests to avoid querying 
    of subschema. (#585)
  * LDAP Resolver: Support StartTLS over Port 389.
  * Simplify LDAP Resolver: Remove username from Attribute Mapping.
  * Simplefy LDAP Resolver: Remove reverse filter.

  Misc Enhancements:
  * Automatically add user's mobile number if tokentype is SMS.
  * Add example configuration for GTX messaging SMS gateway.
  * Add a script "privacyidea-get-unused-tokens" to find
    unused tokens
  * WebUI: Add a busy indicator spinner.
  * Improve the pi-manage script in regards to backup and restore.
    Let you choose whether to backup encryption key or not.
    Better handling for individual pathes. (#626, #623)

  Fixes:
  * LDAP Resolver: Verify SSL Certificate (Security)
  * LDAP Resolver: Allow special characters in NTLM password
  * LDAP Resolver: Allow searching for users with German umlaut
  * Remove the "unsafe" notation in the QR-Code link, so that 
    a smartphone may import the key during HOTP/TOTP token enrollment
    by clicking the link. (#620)
  * Use defusexml to avoid XML bombs on token import (Security)
  * Replace eval with ast.literal_evel (Security)
  * Add missing attributes for U2F tokens in 
    validate/triggerchallenge API
  * Let /validate/triggerchallenge write to audit log.
  * Fix mangle policy for users and realms
  * Avoid logging of password in check_user_pass in debug level 
    (level=10)
  * Set encrypted PIN on enrollment for certificate tokens (#625)
  * Remove unused policy action "motp_webprovision"
  * Allow emailtext policy in triggerchallenge API (#642)
 
* Tue Jan 10 2017 NetKnights GmbH <release@netknights.it> 2.17
  Features
  * Token Handler. Using the token handler the administrator
    can defined actions in response to events, to modify tokens
    like deleting, modifying, initilizing... tokens (#532)
  * Script Event Handler or Shell Event Handler allows to
    trigger an external shell script, if some event occurs. (#536)
  * Add additional endpoint to trigger a challenge response
    like the sending of an SMS, if the token PIN is not
    available (#531)
  * Policy Handling to also check for secondary resolvers of
    a user. This way a user can authenticate with his primary 
    resolver but policy will also work for secondary resolvers (#543)

  Enhancements
  * The event handler conditions also determine a serial number
    even if there is no serial number in the request:
    If the user from the request only has one token assigned. (#571)
  * Allow event definitions to be disabled (#537)
  * Allow event to be addressed by a destinct name (#522)
  * Improving LDAP performace by addressing different functionality 
    of ldap3 version 1.x and 2.x. (#549)
  * Improve SQL Audit by adding the SQL Audit table to the schema.
    Table is not created during HTTP request. (#557)
  * Limit audit log entry age. Users may only view audit
    log entries up to a certain age. (#541)
  * Add checkbox to only display used actions in a policy (#573)
  * In event handler: Use serial number of a user's token if the
    user has only one token (#571)
  * Download a filtered audit log (#539)

  Fixes
  * Add missing token serial number to audit log if token is
    deletes (#546)
  * Fix event handler saving (#551)
  * HttpSMSProvider accepts status codes 201 and 202 in addition
    to 200 (#562)
  * Fix checkbox bug in NOREFERRALS of LDAP resolver (#563)
  * Add documentation for SMS provider (#566)
  * Remove 301 redirects from WebUI (#576)


* Fri Dec 02 2016 NetKnights GmbH <release@netknights.it> 2.16.1
  Featurs
  * Add HSM support via AES keys (#534)
  * Improved Event Handler for flexible notification (#511)
  * Signed subscription files for adding and checking
    for extra functionality during authentication request (#502)

  Enhancements
  * Allow additional filter attributes in the Audit Log (#519)
  * Show or hide realms in the login dialog via policy (#517)
  * Improve UI if admin is not allowed for certain actions (#516, #512)
  * Disable OTP PIN during enrollment via policy (#439)
  * Allow automatic sending of registration code via email (#514)

  Fixes
  * Allow compatibility with ldap3 >= 2.0.7 (#533 #535)
  * Fix problem with Notification when no tokenowner is available (#528)
  * Fix confusion of client HTTP parameters (#529)
  * Fix enabled flag with certain database types (#527)
  * Catch error in case of faulty overrideClient definition (#526)
  * Truncate Audit lines, that are too long for the DB table (#525)


* Tue Oct 11 2016 NetKnights GmbH <release@netknights.it> 2.15
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


* Wed Aug 24 2016 NetKnights GmbH <release@netknights.it> 2.14
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

* Thu Jun 30 2016 NetKnights GmbH <release@netknights.it> 2.13
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

* Thu Feb 11 2016 NetKnights GmbH <release@netknights.it> 2.10
- User Registration: A user may register himself and thus create
  his new user account.
- Password Reset: Using a recovery token a user may issue a
  password reset without bothering the administrator or the help desk.
- Enrollment Wizard for easy user token enrollment
- SMTP Servers: Define several system wide SMTP settings and use
  these for Email token, SMTP SMS Provider, registration process,
  or password reset.

* Tue Jan 26 2016 NetKnights GmbH <release@netknights.it> 2.10dev5-1
- initial RPM packaging

