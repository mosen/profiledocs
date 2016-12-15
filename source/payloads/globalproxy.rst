Global HTTP Proxy
=================

This payload allows you to specify global HTTP proxy settings.

.. NOTE:: If the ProxyType field is set to Auto and no ProxyPACURL value is specified,
    the device uses the web proxy autodiscovery protocol (WPAD) to discover proxies.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.proxy.http.global manifest.plist
.. pfm:: manifests/manual/com.apple.proxy.http.global manifest.plist

Keys
----

.. pfmkey:: ProxyType manifests/manual/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyServer manifests/manual/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyServerPort manifests/manual/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyUsername manifests/manual/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPassword manifests/manual/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPACURL manifests/manual/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyPACFallbackAllowed manifests/manual/com.apple.proxy.http.global manifest.plist
.. pfmkey:: ProxyCaptiveLoginAllowed manifests/manual/com.apple.proxy.http.global manifest.plist