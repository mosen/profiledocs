Global HTTP Proxy
=================

This payload allows you to specify global HTTP proxy settings.

There can only be one of this payload at any time. This payload can only be installed on a supervised device.

.. NOTE:: If the ProxyType field is set to Auto and no ProxyPACURL value is specified,
    the device uses the web proxy autodiscovery protocol (WPAD) to discover proxies.


.. pfm:: com.apple.proxy.http.global manifest.plist

Keys
----

.. pfmkey:: ProxyType com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyServer com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyServerPort com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyUsername com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPassword com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPACURL com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPACFallbackAllowed com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyCaptiveLoginAllowed com.apple.proxy.http.global manifest.plist