.. _payloadtype-com.apple.security.firewall:

Firewall
========

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.security.firewall.png
    :align: right
    :figwidth: 200px

:download:`Template <../_static/examples/com.apple.security.firewall.mobileconfig>`

Available in macOS 10.12 and later. A Firewall payload manages the Application Firewall settings accessible in the Security Preferences pane. Note these restrictions:

- The payload must exist in a system-scoped profile.
- If more than one profile contains this payload, the most restrictive union of settings will be used.

.. warning:: Apple claims that:
    The "Automatically allow signed downloaded software" and "Automatically allow built-in software" options are not supported, but both will be forced **ON** when this payload is present.
    However those options are not changed when the payload is installed. Only the UI is greyed out.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.security.firewall manifest.plist

Keys
----

.. pfmkey:: EnableFirewall /_static/manifests/com.apple.security.firewall manifest.plist
.. pfmkey:: BlockAllIncoming /_static/manifests/com.apple.security.firewall manifest.plist
.. pfmkey:: EnableStealthMode /_static/manifests/com.apple.security.firewall manifest.plist
.. pfmkey:: Applications /_static/manifests/com.apple.security.firewall manifest.plist

Each item in the applications list contains these keys:

.. pfmkey:: Applications:ApplicationItem:BundleID /_static/manifests/com.apple.security.firewall manifest.plist
.. pfmkey:: Applications:ApplicationItem:Allowed /_static/manifests/com.apple.security.firewall manifest.plist

