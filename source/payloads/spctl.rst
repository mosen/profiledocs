System Policy Control
=====================

This payload allows control over configuring the “Allowed applications downloaded from:” option in the “General” tab of “Security & Privacy” in System Preferences.

This payload must only exist in a device profile. If the payload is present in a user profile, an error will be generated during installation and the profile will fail to install.

.. pfm:: manifests/manual/com.apple.systempolicy.control manifest.plist

Requirements
------------

- macOS 10.8+

Keys
----

.. pfmkey:: EnableAssessment manifests/manual/com.apple.systempolicy.control manifest.plist
.. pfmkey:: AllowIdentifiedDevelopers manifests/manual/com.apple.systempolicy.control manifest.plist