.. _payloadtype-com.apple.security.pkcs12:

Certificate (PKCS#12)
=====================
:download:`Template <../_static/examples/com.apple.security.pkcs12.mobileconfig>`

Password-protected identity certificate (.p12). Only one certificate may be included.

.. WARNING:: Because the password string is stored in the clear in the profile, it is recommended that the profile be encrypted for the device.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.security.pkcs12 manifest.plist

Keys
----

.. pfmkey:: PayloadCertificateFileName /_static/manifests/com.apple.security.pkcs12 manifest.plist
.. pfmkey:: PayloadContent /_static/manifests/com.apple.security.pkcs12 manifest.plist
.. pfmkey:: Password /_static/manifests/com.apple.security.pkcs12 manifest.plist


Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW248>`_.

