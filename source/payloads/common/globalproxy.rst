.. _payloadtype-com.apple.proxy.http.global:

Global HTTP Proxy
=================

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.proxy.http.global.png
    :align: right
    :figwidth: 200px


:download:`Template <../_static/examples/com.apple.proxy.http.global.mobileconfig>`

This payload allows you to specify global HTTP proxy settings.

In some workflows (eg. Provisional DEP with Configurator 2) you must use the Wi-Fi proxy setting because the device
will not be supervised until the workflow completes.

.. NOTE:: If the ProxyType field is set to Auto and no ProxyPACURL value is specified,
    the device uses the web proxy autodiscovery protocol (WPAD) to discover proxies.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.proxy.http.global manifest.plist

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
