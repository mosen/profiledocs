.. _payloadtype-com.apple.systemmigration:

System Migration
================
:download:`Template </_static/examples/com.apple.systemmigration.mobileconfig>`

System migration occurs when items are transferred to a macOS device from a Windows device by reading source and
destination path pairs from plist files. This payload provides a way to customize those transfers.

This payload must be single and exist only in a device profile. If the payload is present in a user profile,
an error will be generated during installation and the profile will fail to install.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.systemmigration manifest.plist

Keys
----

CustomBehavior
^^^^^^^^^^^^^^

CustomBehaviour contains an array of dicts conforming to the following specification:

.. pfm:: /_static/manifests/com.apple.systemmigration manifest.plist
    :key: CustomBehavior:CustomBehaviorItem


Paths
^^^^^

Paths contains an array of dicts conforming to the following specification:

.. pfm:: /_static/manifests/com.apple.systemmigration manifest.plist
    :key: CustomBehavior:CustomBehaviorItem:Paths:PathsItem

Links
-----

- `Official Documentation <https://developer.apple.com/library/prerelease/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW221>`_.
