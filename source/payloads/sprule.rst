System Policy Rule
==================

This is one of three payloads that allows control of various GateKeeper settings.

This payload allows control over Gatekeeper’s system policy rules.
The keys and functionality are tightly related to the spctl command line tool. You should be read the manual page for spctl.

This payload must only exist in a device profile.
If the payload is present in a user profile, an error will be generated during installation and the profile will fail to install.

.. pfm:: manifests/manual/com.apple.systempolicy.rule manifest.plist

Requirements
------------

- macOS 10.8+

Keys
----

.. pfmkey:: Requirement manifests/manual/com.apple.systempolicy.rule manifest.plist
.. pfmkey:: Comment manifests/manual/com.apple.systempolicy.rule manifest.plist
.. pfmkey:: Expiration manifests/manual/com.apple.systempolicy.rule manifest.plist
.. pfmkey:: OperationType manifests/manual/com.apple.systempolicy.rule manifest.plist