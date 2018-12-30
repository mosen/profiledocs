.. _payloadtype-com.apple.eas.account:

Exchange
========
:download:`Template </_static/examples/com.apple.eas.account.mobileconfig>`

In iOS, the Exchange payload is designated by specifying **com.apple.eas.account** as the PayloadType value. This payload configures an Exchange Active Sync account on the device.

In macOS, the Exchange payload is designated by specifying **com.apple.ews.account** as the PayloadType value. This payload will configure an Exchange Web Services account for Contacts, Mail, Notes, Reminders, and Calendar.

.. NOTE:: As with VPN and Wi-Fi configurations, it is possible to associate an SCEP credential with an Exchange configuration via the PayloadCertificateUUID key.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.eas.account manifest.plist

Keys
----

.. pfmkey:: Certificate /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: CertificateName /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: CertificatePassword /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: PayloadCertificateUUID /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: Host /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: MailNumberOfPastDaysToSync /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: SSL /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: EmailAddress /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: UserName /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: Password /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: PreventMove /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: PreventAppSheet /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: allowMailDrop /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEnabled /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEnablePerMessageSwitch /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: SMIMESigningCertificateUUID /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: SMIMEEncryptionCertificateUUID /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: disableMailRecentsSyncing /_static/manifests/com.apple.eas.account manifest.plist
.. pfmkey:: CommunicationServiceRules /_static/manifests/com.apple.eas.account manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW25>`_.
