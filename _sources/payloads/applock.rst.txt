App Lock
========

Only one of this payload type can be installed at any time. This payload can be installed only on a Supervised device.
By installing an app lock payload, the device is locked to a single application until the payload is removed. The home button is disabled, and the device returns to the specified application automatically upon wake or reboot.

.. pfm:: manifests/ac2/com.apple.app.lock manifest.plist

Requirements
------------

- iOS 6.0+

Keys
----

.. pfmkey:: App manifests/ac2/com.apple.app.lock manifest.plist

