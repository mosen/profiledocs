.. _payloadtype-com.apple.desktop:

Desktop Payload
===============

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.desktop.png
    :align: right
    :figwidth: 200px

:download:`Template <../_static/examples/com.apple.desktop.mobileconfig>`

This payload sets up macOS Desktop settings and restrictions. It is supported on the user channel and on macOS 10.10 and later.

.. note:: The locked setting value isnt actually respected. If locked is present and false the desktop picture will
    still be locked.

.. contents::

Summary
-------

.. pfmheader:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.desktop.plist

Keys
----

.. pfmkey:: locked /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.desktop.plist
.. pfmkey:: override-picture-path /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.desktop.plist
