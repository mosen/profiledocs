.. _payloadtype-com.apple.airprint:

AirPrint
========
:download:`Template <../_static/examples/com.apple.airprint.mobileconfig>`

The AirPrint payload adds AirPrint printers to the user’s AirPrint printer list. This makes it easier to support environments where the printers and the devices are on different subnets.

.. contents::

Summary
-------

.. pfmheader::  /_static/manifests/com.apple.airprint manifest.plist

Keys
----

.. pfmkey:: AirPrint /_static/manifests/com.apple.airprint manifest.plist

AirPrint items are in the following format:

.. pfm:: /_static/manifests/com.apple.airprint manifest.plist
    :key: AirPrint:Identifier

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW39>`_.