.. _payloadtype-com.apple.font:

Font
====
:download:`Template <../_static/examples/com.apple.font.mobileconfig>`

A Font payload lets you add an additional font to an iOS device.

Each payload must contain exactly one font file in TrueType (.ttf) or OpenType (.otf) format.
Collection formats (.ttc or .otc) are not supported.

.. WARNING:: Fonts are identified by their embedded PostScript names.
    Two fonts with the same PostScript name are considered to be the same font even if their contents differ.
    Installing two different fonts with the same PostScript name is not supported, and the resulting behavior is undefined.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.font manifest.plist

Keys
----

.. pfmkey:: Name /_static/manifests/com.apple.font manifest.plist
.. pfmkey:: Font /_static/manifests/com.apple.font manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW43>`_.
