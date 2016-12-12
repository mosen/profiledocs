Global HTTP Proxy
=================

This payload allows you to specify global HTTP proxy settings.

There can only be one of this payload at any time. This payload can only be installed on a supervised device.

.. NOTE:: If the ProxyType field is set to Auto and no ProxyPACURL value is specified,
    the device uses the web proxy autodiscovery protocol (WPAD) to discover proxies.


.. pfm:: manifests/ac2/com.apple.proxy.http.global manifest.plist

Keys
----

.. pfmkey:: ProxyType manifests/ac2/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyServer manifests/ac2/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyServerPort manifests/ac2/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyUsername manifests/ac2/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPassword manifests/ac2/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPACURL manifests/ac2/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPACFallbackAllowed manifests/ac2/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyCaptiveLoginAllowed manifests/ac2/com.apple.proxy.http.global manifest.plist