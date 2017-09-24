.. _payloadtype-com.apple.MCX.FileVault2:

FileVault 2
===========
:download:`Template <../_static/examples/com.apple.MCX.FileVault2.mobileconfig>`

You can use FileVault 2 to perform full XTS-AES 128 encryption on the contents of a volume.
Removal of the FileVault payload does not disable FileVault.

A personal recovery user will normally be created unless the UseRecoveryKey key value is false.

An institutional recovery key will be created only if either there is certificate data available in the Certificate key value,
a specific certificate payload is referenced, or the UseKeychain key value is set to true and a valid FileVaultMaster.keychain file was created.

In all cases, the certificate information must be set up properly for FileVault or it will be ignored and no institutional recovery key will be set up.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.MCX.FileVault2 manifest.plist

Keys
----

.. pfmkey:: Enable /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: Defer /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: UserEntersMissingInfo /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: UseRecoveryKey /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: ShowRecoveryKey /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: OutputPath /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: Certificate /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: PayloadCertificateUUID /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: Username /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: Password /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: UseKeychain /_static/manifests/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: DeferForceAtUserLoginMaxBypassAttempts /_static/manifests/com.apple.MCX.FileVault2 manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW842>`_.


