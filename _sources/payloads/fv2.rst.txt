FileVault 2
===========

You can use FileVault 2 to perform full XTS-AES 128 encryption on the contents of a volume.
Removal of the FileVault payload does not disable FileVault.

A personal recovery user will normally be created unless the UseRecoveryKey key value is false.

An institutional recovery key will be created only if either there is certificate data available in the Certificate key value,
a specific certificate payload is referenced, or the UseKeychain key value is set to true and a valid FileVaultMaster.keychain file was created.

In all cases, the certificate information must be set up properly for FileVault or it will be ignored and no institutional recovery key will be set up.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfm:: manifests/manual/com.apple.MCX.FileVault2 manifest.plist

Keys
----

.. pfmkey:: Enable manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: Defer manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: UserEntersMissingInfo manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: UseRecoveryKey manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: ShowRecoveryKey manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: OutputPath manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: Certificate manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: PayloadCertificateUUID manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: Username manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: Password manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: UseKeychain manifests/manual/com.apple.MCX.FileVault2 manifest.plist
.. pfmkey:: DeferForceAtUserLoginMaxBypassAttempts manifests/manual/com.apple.MCX.FileVault2 manifest.plist

