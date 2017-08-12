.. _payloadtype-com.apple.desktop:

Desktop Picture
===============
:download:`Template <../_static/examples/com.apple.desktop.mobileconfig>`

This payload sets up macOS Desktop settings and restrictions. It is supported on the user channel and on macOS 10.10 and later.

.. note:: The locked setting value isnt actually respected. If locked is present and false the desktop picture will
    still be locked.

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.desktop manifest.plist
.. pfm:: /_static/manifests/com.apple.desktop manifest.plist

