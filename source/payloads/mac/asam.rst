.. _payloadtype-com.apple.asam:

Autonomous Single App Mode
==========================

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.asam.png
    :align: right
    :figwidth: 200px

:download:`Template <../_static/examples/com.apple.asam.mobileconfig>`

This payload grants Autonomous Single App Mode capabilities for specific applications. Available in macOS 10.13.4 and later.

It must be installed as a device profile. Only one payload of this type can be installed on a system. This payload can only be installed via a "user approved" MDM server.

.. contents::

Summary
-------

.. pfmheader:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.asam.plist

Keys
----

.. pfmkey:: AllowedApplications /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.asam.plist

Each item contains the following keys

.. pfmkey:: AllowedApplications:AllowedApplicationsItem:BundleIdentifier /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.asam.plist
.. pfmkey:: AllowedApplications:AllowedApplicationsItem:TeamIdentifier /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.asam.plist