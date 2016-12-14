Cellular
========

A cellular payload configures cellular network settings on the device.
It is not supported on macOS. On iOS 7 and later, a cellular payload is designated by specifying manifests/ac2/com.apple.cellular as the PayloadType value.

Cellular payloads have two important installation requirements:

- No more than one cellular payload can be installed at any time.
- A cellular payload cannot be installed if an APN payload is already installed.

This payload replaces the manifests/ac2/com.apple.managedCarrier payload, which is supported, but deprecated.

- Supersedes ``manifests/ac2/com.apple.apn.managed`` (APN).
- Supersedes ``manifests/ac2/com.apple.managedCarrier``

.. pfm:: manifests/ac2/com.apple.cellular manifest.plist

Keys
----

.. pfmkey:: APNs manifests/ac2/com.apple.cellular manifest.plist
.. pfmkey:: AttachAPN manifests/ac2/com.apple.cellular manifest.plist

.. pfm:: manifests/ac2/com.apple.cellular manifest.plist
   :key: AttachAPN