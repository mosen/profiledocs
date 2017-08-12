.. _payloadtype-com.apple.ManagedClient.preferences:

Legacy Custom Settings (MCX)
============================

This payload is the old, MCX style way to apply custom settings.
It respects some of the semantics of ``Set-Once`` from the OS X 10.6 era.

This is a catch-all payload for writing defaults in any given preference domain.
It is the macOS equivalent of :ref:`payloadtype-com.apple.defaults.managed`.

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.ManagedClient.preferences manifest.plist
.. pfm:: /_static/manifests/com.apple.ManagedClient.preferences manifest.plist

Keys
----

.. pfmkey:: PayloadContent /_static/manifests/com.apple.ManagedClient.preferences manifest.plist

PayloadContent Keys
"""""""""""""""""""

.. pfm:: /_static/manifests/com.apple.ManagedClient.preferences manifest.plist
   :key: PayloadContent:PreferenceDomainHere

