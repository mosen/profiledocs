Exchange
========

In iOS, the Exchange payload is designated by specifying com.apple.eas.account as the PayloadType value. This payload configures an Exchange Active Sync account on the device.

In macOS, the Exchange payload is designated by specifying com.apple.ews.account as the PayloadType value. This payload will configure an Exchange Web Services account for Contacts, Mail, Notes, Reminders, and Calendar.

.. NOTE:: As with VPN and Wi-Fi configurations, it is possible to associate an SCEP credential with an Exchange configuration via the PayloadCertificateUUID key.

.. pfm:: com.apple.eas.account manifest.plist

Keys
----

.. pfmkey:: Certificate com.apple.eas.account manifest.plist
.. pfmkey:: CertificateName com.apple.eas.account manifest.plist
.. pfmkey:: CertificatePassword com.apple.eas.account manifest.plist
.. pfmkey:: PayloadCertificateUUID com.apple.eas.account manifest.plist
.. pfmkey:: Host com.apple.eas.account manifest.plist
.. pfmkey:: MailNumberOfPastDaysToSync com.apple.eas.account manifest.plist
.. pfmkey:: SSL com.apple.eas.account manifest.plist
.. pfmkey:: EmailAddress com.apple.eas.account manifest.plist
.. pfmkey:: UserName com.apple.eas.account manifest.plist
.. pfmkey:: Password com.apple.eas.account manifest.plist
.. pfmkey:: PreventMove com.apple.eas.account manifest.plist
.. pfmkey:: PreventAppSheet com.apple.eas.account manifest.plist
.. pfmkey:: allowMailDrop com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEnabled com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEnablePerMessageSwitch com.apple.eas.account manifest.plist
.. pfmkey:: SMIMESigningCertificateUUID com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEncryptionCertificateUUID com.apple.eas.account manifest.plist
.. pfmkey:: disableMailRecentsSyncing com.apple.eas.account manifest.plist
.. pfmkey:: CommunicationServiceRules com.apple.eas.account manifest.plist