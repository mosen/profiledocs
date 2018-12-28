.. _payloadtype-com.apple.security.FDERecoveryKeyEscrow:

FDE Recovery Key Escrow Payload
===============================

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.security.FDERecoveryKeyEscrow.png
    :align: right
    :figwidth: 200px

:download:`Template <../_static/examples/com.apple.security.FDERecoveryKeyEscrow.mobileconfig>`

By default, FileVault recovery keys are sent to Apple if the user requests.

If FileVault is enabled after this profile is installed, the FileVault PRK will be encrypted with the specified
certificate, wrapped in a CMS envelope and written to a file at :file:`/var/db/FileVaultPRK.dat`.

This data will also be made available as part of a response to an MDM ``SecurityInfo`` command.

Caveats mentioned in the official guide:

- Must be system scoped
- Installing multiple payloads results in an error.
- The previous, deprecated payload (com.apple.security.FDERecoveryRedirect) can be installed but will be ignored.
- If only the old payload is installed when FileVault is turned on, it will cause an error.
- If FileVault was already enabled and escrowed with the old payload, no warning or error will be shown.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.security.FDERecoveryKeyEscrow manifest.plist

Keys
----

.. pfmkey:: Location /_static/manifests/com.apple.security.FDERecoveryKeyEscrow manifest.plist
.. pfmkey:: EncryptCertPayloadUUID /_static/manifests/com.apple.security.FDERecoveryKeyEscrow manifest.plist
.. pfmkey:: DeviceKey /_static/manifests/com.apple.security.FDERecoveryKeyEscrow manifest.plist
