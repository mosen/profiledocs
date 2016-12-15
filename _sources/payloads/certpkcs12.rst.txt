Certificate (PKCS#12)
=====================

Password-protected identity certificate. Only one certificate may be included.

.. WARNING:: Because the password string is stored in the clear in the profile, it is recommended that the profile be encrypted for the device.

Summary
-------

.. pfmheader:: manifests/ac2/com.apple.security.pkcs12 manifest.plist
.. pfm:: manifests/ac2/com.apple.security.pkcs12 manifest.plist

Keys
----

.. pfmkey:: PayloadCertificateFileName manifests/ac2/com.apple.security.pkcs12 manifest.plist
.. pfmkey:: PayloadContent manifests/ac2/com.apple.security.pkcs12 manifest.plist
.. pfmkey:: Password manifests/ac2/com.apple.security.pkcs12 manifest.plist