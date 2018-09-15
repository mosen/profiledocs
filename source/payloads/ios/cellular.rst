.. _payloadtype-com.apple.cellular:

Cellular
========
:download:`Template <../_static/examples/com.apple.cellular.mobileconfig>`

A cellular payload configures cellular network settings on the device.
It is not supported on macOS. On iOS 7 and later, a cellular payload is designated by specifying **com.apple.cellular** as the PayloadType value.

Cellular payloads have two important installation requirements:

- No more than one cellular payload can be installed at any time.
- A cellular payload cannot be installed if an APN payload is already installed.

This payload replaces the com.apple.managedCarrier payload, which is supported, but deprecated.

- Supersedes ``com.apple.apn.managed`` (APN) which is used on iOS 6 and earlier.
- Supersedes ``com.apple.managedCarrier``

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.cellular manifest.plist

Keys
----

.. pfmkey:: APNs /_static/manifests/com.apple.cellular manifest.plist
.. pfmkey:: AttachAPN /_static/manifests/com.apple.cellular manifest.plist

.. pfm:: /_static/manifests/com.apple.cellular manifest.plist
   :key: AttachAPN

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW48>`_.
