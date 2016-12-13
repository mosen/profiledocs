Shared Device
=============

The Shared Device Configuration Payload allows admins to specify optional text displayed on the login window and
lock screen (i.e. a "If Lost, Return To" message and Asset Tag Information).

.. pfm:: manifests/ac2/com.apple.shareddeviceconfiguration manifest.plist

Requirements
------------

iOS
    9.3+
Supervised
    YES
Scope
    System



Keys
----

.. pfmkey:: IfLostReturnToMessage manifests/ac2/com.apple.shareddeviceconfiguration manifest.plist
.. pfmkey:: AssetTagInformation manifests/ac2/com.apple.shareddeviceconfiguration manifest.plist