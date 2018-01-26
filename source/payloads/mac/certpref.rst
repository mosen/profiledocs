.. _payloadtype-com.apple.security.certificatepreference:

Certificate Preference
======================
:download:`Template <../_static/examples/com.apple.security.certificatepreference.mobileconfig>`

A Certificate Preference payload lets you identify a Certificate Preference item in the user's keychain that references
a certificate payload included in the same profile. It can only appear in a user profile, not a device profile.

You can include multiple Certificate Preference payloads as needed.
Certificate Preference payloads are designated by specifying com.apple.security.certificatepreference
as the PayloadType value.

See also :ref:`payloadtype-com.apple.security.identitypreference` for setting up identity preferences.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.security.certificatepreference manifest.plist

Keys
----

.. pfmkey:: Name /_static/manifests/com.apple.security.certificatepreference manifest.plist
.. pfmkey:: PayloadCertificateUUID /_static/manifests/com.apple.security.certificatepreference manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW143>`_.
