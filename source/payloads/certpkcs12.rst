Certificate (PKCS#12)
=====================

Password-protected identity certificate. Only one certificate may be included.

.. WARNING:: Because the password string is stored in the clear in the profile, it is recommended that the profile be encrypted for the device.


.. pfm:: com.apple.security.pkcs12 manifest.plist

Keys
----

.. pfmkey:: PayloadCertificateFileName com.apple.security.pkcs12 manifest.plist
.. pfmkey:: PayloadContent com.apple.security.pkcs12 manifest.plist
.. pfmkey:: Password com.apple.security.pkcs12 manifest.plist