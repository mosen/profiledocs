Exchange
========

In iOS, the Exchange payload is designated by specifying com.apple.eas.account as the PayloadType value. This payload configures an Exchange Active Sync account on the device.

In macOS, the Exchange payload is designated by specifying com.apple.ews.account as the PayloadType value. This payload will configure an Exchange Web Services account for Contacts, Mail, Notes, Reminders, and Calendar.

.. NOTE:: As with VPN and Wi-Fi configurations, it is possible to associate an SCEP credential with an Exchange configuration via the PayloadCertificateUUID key.

.. pfm:: manifests/ac2/com.apple.eas.account manifest.plist

Keys
----

.. pfmkey:: Certificate manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: CertificateName manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: CertificatePassword manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: PayloadCertificateUUID manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: Host manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: MailNumberOfPastDaysToSync manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: SSL manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: EmailAddress manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: UserName manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: Password manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: PreventMove manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: PreventAppSheet manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: allowMailDrop manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEnabled manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEnablePerMessageSwitch manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: SMIMESigningCertificateUUID manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEncryptionCertificateUUID manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: disableMailRecentsSyncing manifests/ac2/com.apple.eas.account manifest.plist
.. pfmkey:: CommunicationServiceRules manifests/ac2/com.apple.eas.account manifest.plist