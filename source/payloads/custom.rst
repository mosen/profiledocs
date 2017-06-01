.. _payloadtype-com.apple.ManagedClient.preferences:

Custom Settings (MCX)
=====================

This is a catch-all payload for writing defaults in any given preference domain.
It is the macOS equivalent of :ref:`payloadtype-com.apple.defaults.managed`.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.ManagedClient.preferences manifest.plist
.. pfm:: manifests/manual/com.apple.ManagedClient.preferences manifest.plist

Keys
----

.. pfmkey:: PayloadContent manifests/manual/com.apple.ManagedClient.preferences manifest.plist

PayloadContent Keys
"""""""""""""""""""

.. pfm:: manifests/manual/com.apple.ManagedClient.preferences manifest.plist
   :key: PayloadContent:PreferenceDomainHere


Forced
""""""

Forced is an array containing a dictionary in the following format:

.. pfm:: manifests/manual/com.apple.ManagedClient.preferences manifest.plist
   :key: PayloadContent:PreferenceDomainHere:Forced:ForcedItem


