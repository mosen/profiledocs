.. _payloadtype-com.apple.systempolicy.control:

System Policy Control
=====================

This payload allows control over configuring the “Allowed applications downloaded from:” option in the “General” tab of “Security & Privacy” in System Preferences.

This payload must only exist in a device profile. If the payload is present in a user profile, an error will be generated during installation and the profile will fail to install.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.systempolicy.control manifest.plist

Keys
----

.. pfmkey:: EnableAssessment /_static/manifests/com.apple.systempolicy.control manifest.plist
.. pfmkey:: AllowIdentifiedDevelopers /_static/manifests/com.apple.systempolicy.control manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW21>`_.
