.. _payloadtype-com.apple.mdm:

MDM
===

This payload, when installed, will attempt to enroll the device into an MDM server.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.mdm manifest.plist

Keys
----

.. pfmkey:: IdentityCertificateUUID /_static/manifests/com.apple.mdm manifest.plist
.. pfmkey:: Topic /_static/manifests/com.apple.mdm manifest.plist
.. pfmkey:: ServerURL /_static/manifests/com.apple.mdm manifest.plist

Must begin with the https:// URL scheme, and may contain a port number (:1234, for example).

.. pfmkey:: ServerCapabilities /_static/manifests/com.apple.mdm manifest.plist
.. pfmkey:: SignMessage /_static/manifests/com.apple.mdm manifest.plist
.. pfmkey:: CheckInURL /_static/manifests/com.apple.mdm manifest.plist
.. pfmkey:: CheckOutWhenRemoved /_static/manifests/com.apple.mdm manifest.plist
.. pfmkey:: AccessRights /_static/manifests/com.apple.mdm manifest.plist
.. pfmkey:: UseDevelopmentAPNS /_static/manifests/com.apple.mdm manifest.plist


Access Rights
-------------

MDM Access Rights can be constructed from a bitmask by ORing the following values:

- 1: Allow inspection of installed configuration profiles.
- 2: Allow installation and removal of configuration profiles.
- 4: Allow device lock and passcode removal.
- 8: Allow device erase.
- 16: Allow query of Device Information (device capacity, serial number).
- 32: Allow query of Network Information (phone/SIM numbers, MAC addresses).
- 64: Allow inspection of installed provisioning profiles.
- 128: Allow installation and removal of provisioning profiles.
- 256: Allow inspection of installed applications.
- 512: Allow restriction-related queries.
- 1024: Allow security-related queries.
- 2048: Allow manipulation of settings. Availability: Available in iOS 5.0 and later. Available in OS X 10.9 for certain commands.
- 4096: Allow app management. Availability: Available in iOS 5.0 and later. Available in OS X 10.9 for certain commands.
    May not be zero. If 2 is specified, 1 must also be specified. If 128 is specified, 64 must also be specified.

Links
-----

- `Structure of MDM Payloads <https://developer.apple.com/library/prerelease/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW50>`_.

