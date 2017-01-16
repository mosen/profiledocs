.. _payloadtype-com.apple.vpn.managed.applayer:

Per-App VPN
===========

The Per-App VPN payload is used for configuring add-on VPN software, and it works only on VPN services of type 'VPN'.
It should not be confused with the standard VPN payload, described in :ref:`payloadtype-com.apple.vpn.managed`.

The Per-App VPN payload supports all of the keys described in :ref:`payloadtype-com.apple.vpn.managed` plus the following additional keys

.. note:: Copy VPN payload keys into the per app vpn manifest.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.vpn.managed.applayer manifest.plist

.. pfm:: manifests/manual/com.apple.vpn.managed.applayer manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW37>`_.
