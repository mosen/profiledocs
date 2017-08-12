.. _payloadtype-com.apple.proxy.http.global:

Global HTTP Proxy
=================
:download:`Template <../_static/examples/com.apple.proxy.http.global.mobileconfig>`

This payload allows you to specify global HTTP proxy settings.

.. NOTE:: If the ProxyType field is set to Auto and no ProxyPACURL value is specified,
    the device uses the web proxy autodiscovery protocol (WPAD) to discover proxies.

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.proxy.http.global manifest.plist
.. pfm:: /_static/manifests/com.apple.proxy.http.global manifest.plist

Keys
----

.. pfmkey:: ProxyType /_static/manifests/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyServer /_static/manifests/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyServerPort /_static/manifests/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyUsername /_static/manifests/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPassword /_static/manifests/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPACURL /_static/manifests/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPACFallbackAllowed /_static/manifests/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyCaptiveLoginAllowed /_static/manifests/com.apple.proxy.http.global manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW34>`_.
