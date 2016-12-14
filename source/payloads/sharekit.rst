.. _payloadtype-com.apple.ShareKitHelper:

ShareKit
========

It can contain only one payload. It is supported on the User Channel.
The ShareKit Payload specifies which ShareKit plugin can be accessed on client. Both allow and disallow lists can be specified.

.. pfm:: manifests/manual/com.apple.ShareKitHelper manifest.plist

Requirements
------------

- macOS 10.9+

Keys
----

.. pfmkey:: SHKAllowedShareServices manifests/manual/com.apple.ShareKitHelper manifest.plist
.. pfmkey:: SHKDeniedShareServices manifests/manual/com.apple.ShareKitHelper manifest.plist
