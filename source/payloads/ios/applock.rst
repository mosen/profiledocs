.. _payloadtype-com.apple.app.lock:

App Lock
========
:download:`Template <../_static/examples/com.apple.app.lock.mobileconfig>`

Only one of this payload type can be installed at any time. This payload can be installed only on a Supervised device.
By installing an app lock payload, the device is locked to a single application until the payload is removed.
The home button is disabled, and the device returns to the specified application automatically upon wake or reboot.

.. note:: You can’t update any app while the device is locked in Single App Mode.
   You need to exit Single App Mode long enough to update apps as needed.
   During that time you should restrict the visible apps as much as possible,
   except for Settings and Phone and any other apps that cannot be blacklisted.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.applock manifest.plist

Keys
----

.. pfmkey:: App /_static/manifests/ac2/com.apple.applock manifest.plist

App Keys
^^^^^^^^

.. pfm:: /_static/manifests/ac2/com.apple.applock manifest.plist
   :key: App

Options
^^^^^^^

.. pfm:: /_static/manifests/ac2/com.apple.applock manifest.plist
   :key: App:Options

User Enabled Options
^^^^^^^^^^^^^^^^^^^^

.. pfm:: /_static/manifests/ac2/com.apple.applock manifest.plist
   :key: App:UserEnabledOptions

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW35>`_.

