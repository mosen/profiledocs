Font
====

A Font payload lets you add an additional font to an iOS device.

Each payload must contain exactly one font file in TrueType (.ttf) or OpenType (.otf) format.
Collection formats (.ttc or .otc) are not supported.

.. WARNING:: Fonts are identified by their embedded PostScript names.
    Two fonts with the same PostScript name are considered to be the same font even if their contents differ.
    Installing two different fonts with the same PostScript name is not supported, and the resulting behavior is undefined.

.. pfm:: manifests/ac2/com.apple.font manifest.plist

Keys
----

.. pfmkey:: Name manifests/ac2/com.apple.font manifest.plist
.. pfmkey:: Font manifests/ac2/com.apple.font manifest.plist