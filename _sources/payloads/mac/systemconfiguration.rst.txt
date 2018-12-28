.. _payloadtype-com.apple.SystemConfiguration:

SystemConfiguration (Proxies)
=============================

:download:`Template <../_static/examples/com.apple.SystemConfiguration.mobileconfig>`

This profile allows you to change the proxy settings in the advanced dialog of a network interface.

.. warning:: This is part of the older MCX style profiles, so keys need to be tested.

.. note:: Manifest is incomplete WRT keys for HTTPS/Gopher/FTP proxies

There doesn't seem to be any keys that deal with:

- PAC file URL
- Proxy Authentication Username/Password
- Exclusion of simple hostnames
- FTP Passive Mode
- Which interface the payload applies to

.. todo:: Try combining this with :ref:`payloadtype-com.apple.proxy.http.global`.


.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.SystemConfiguration manifest.plist

Keys
----

.. pfm:: /_static/manifests/com.apple.SystemConfiguration manifest.plist
    :key: Proxies

.. pfmkey:: Proxies:FTPEnable /_static/manifests/com.apple.SystemConfiguration manifest.plist
.. pfmkey:: Proxies:GopherEnable /_static/manifests/com.apple.SystemConfiguration manifest.plist
.. pfmkey:: Proxies:HTTPEnable /_static/manifests/com.apple.SystemConfiguration manifest.plist
.. pfmkey:: Proxies:HTTPPort /_static/manifests/com.apple.SystemConfiguration manifest.plist
.. pfmkey:: Proxies:HTTPProxy /_static/manifests/com.apple.SystemConfiguration manifest.plist
.. pfmkey:: Proxies:HTTPSEnable /_static/manifests/com.apple.SystemConfiguration manifest.plist
.. pfmkey:: Proxies:ProxyAutoConfigEnable /_static/manifests/com.apple.SystemConfiguration manifest.plist
.. pfmkey:: Proxies:RTSPEnable /_static/manifests/com.apple.SystemConfiguration manifest.plist
.. pfmkey:: Proxies:SOCKSEnable /_static/manifests/com.apple.SystemConfiguration manifest.plist

.. pfm:: /_static/manifests/com.apple.SystemConfiguration manifest.plist
    :key: Proxies:ExceptionsList
