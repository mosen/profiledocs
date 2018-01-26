*-
-
.. _payloadtype-com.apple.asam:

Autonomous Single App Mode
==========================

:download:`Template <../_static/examples/com.apple.asam.mobileconfig>`

This payload grants Autonomous Single App Mode capabilities for specific applications. Available in macOS 10.13.4 and later.

It must be installed as a device profile. Only one payload of this type can be installed on a system. This payload can only be installed via a "user approved" MDM server.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.asam manifest.plist

Keys
----

.. pfmkey:: AllowedApplications /_static/manifests/com.apple.asam manifest.plist

Each item contains the following keys

.. pfmkey:: AllowedApplications:AllowedApplicationsItem:BundleIdentifier /_static/manifests/com.apple.asam manifest.plist
.. pfmkey:: AllowedApplications:AllowedApplicationsItem:TeamIdentifier /_static/manifests/com.apple.asam manifest.plist
