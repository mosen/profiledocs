Cellular
========

A cellular payload configures cellular network settings on the device.
It is not supported on macOS. On iOS 7 and later, a cellular payload is designated by specifying com.apple.cellular as the PayloadType value.

Cellular payloads have two important installation requirements:

- No more than one cellular payload can be installed at any time.
- A cellular payload cannot be installed if an APN payload is already installed.

This payload replaces the com.apple.managedCarrier payload, which is supported, but deprecated.

- Supersedes ``com.apple.apn.managed`` (APN).
- Supersedes ``com.apple.managedCarrier``

.. pfm:: com.apple.cellular manifest.plist

Keys
----

.. pfmkey:: APNs com.apple.cellular manifest.plist
.. pfmkey:: AttachAPN com.apple.cellular manifest.plist