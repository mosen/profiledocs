.. _payloadtype-com.apple.app.lock:

App Lock Payload
================

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.app.lock.png
   :align: right
   :figwidth: 200px

By installing an app lock payload, the device is locked to a single application until the payload is removed.
The home button is disabled, and the device returns to the specified application automatically upon wake or reboot.

.. note:: You can’t update any app while the device is locked in Single App Mode.
   You need to exit Single App Mode long enough to update apps as needed.
   During that time you should restrict the visible apps as much as possible,
   except for Settings and Phone and any other apps that cannot be blacklisted.

:download:`Template <../_static/examples/com.apple.app.lock.mobileconfig>`

.. contents::

Summary
-------

.. pfmheader:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.app.lock.plist

Keys
----

.. pfmkey:: App /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.app.lock.plist

App Keys
^^^^^^^^

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.app.lock.plist
   :key: App

Options
^^^^^^^

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.app.lock.plist
   :key: App:Options

User Enabled Options
^^^^^^^^^^^^^^^^^^^^

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.app.lock.plist
   :key: App:UserEnabledOptions
