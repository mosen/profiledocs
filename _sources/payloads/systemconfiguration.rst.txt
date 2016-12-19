.. _payloadtype-com.apple.SystemConfiguration:

SystemConfiguration (Proxies)
=============================

This profile allows you to change the proxy settings in the advanced dialog of a network interface.

.. warning:: This is part of the older MCX style profiles, so keys need to be tested.

.. note:: Manifest is incomplete WRT keys for HTTPS/Gopher/FTP proxies

There doesn't seem to be any keys that deal with:

- PAC file URL
- Proxy Authentication Username/Password
- Exclusion of simple hostnames
- FTP Passive Mode
- Which interface the payload applies to

Summary
-------

.. pfmheader:: manifests/manual/com.apple.SystemConfiguration manifest.plist
.. pfm:: manifests/manual/com.apple.SystemConfiguration manifest.plist


