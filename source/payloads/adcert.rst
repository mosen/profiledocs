.. _payloadtype-com.apple.ADCertificate.managed:

Active Directory Certificate
============================
:download:`Template <../_static/examples/com.apple.ADCertificate.managed.mobileconfig>`

You can request a certificate from a Microsoft Certificate Authority (CA) using DCE/RPC and the
Active Directory Certificate profile payload instructions detailed at https://support.apple.com/kb/HT5357.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.ADCertificate.managed manifest.plist

.. pfm:: manifests/manual/com.apple.ADCertificate.managed manifest.plist


Keys
----

.. pfmkey:: Description manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: CertServer manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: CertTemplate manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: CertificateAuthority manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: CertificateAcquisitionMechanism manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: CertificateRenewalTimeInterval manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: Keysize manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: UserName manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: Password manifests/manual/com.apple.ADCertificate.managed manifest.plist
.. pfmkey:: PromptForCredentials manifests/manual/com.apple.ADCertificate.managed manifest.plist

.. warning:: PromptForCredentials seems to have no effect on manually installed profiles. They still ask for credentials.

.. pfmkey:: AllowAllAppsAccess manifests/manual/com.apple.ADCertificate.managed manifest.plist

Links
-----

- `macmules blog: OSX & AD CERTIFICATE REQUESTS, SOME TIPS <https://macmule.com/2015/09/06/osx-ad-certificate-requests-some-tips/>`_.
- `Certificate Renewal Behaviour <https://support.apple.com/en-us/HT204446>`_.

Troubleshooting
---------------

- If you request a `User` certificate but the payload is in the `System` PayloadScope, the User certificate will be requested as the
  computer account. Normally the certificate policy will deny this, so check that you have the correct scope.

Uninstall Behaviour
-------------------

- The certificate is not revoked upon uninstallation.
- The certificate is not removed from keychain, but the private key IS removed. The private key is named after the issuing host.


