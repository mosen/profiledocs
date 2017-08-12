.. _payloadtype-com.apple.systempolicy.rule:

System Policy Rule
==================

This is one of three payloads that allows control of various GateKeeper settings.

This payload allows control over Gatekeeper’s system policy rules.
The keys and functionality are tightly related to the spctl command line tool. You should be read the manual page for spctl.

This payload must only exist in a device profile.
If the payload is present in a user profile, an error will be generated during installation and the profile will fail to install.

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.systempolicy.rule manifest.plist
.. pfm:: /_static/manifests/com.apple.systempolicy.rule manifest.plist

Keys
----

.. pfmkey:: Requirement /_static/manifests/com.apple.systempolicy.rule manifest.plist
.. pfmkey:: Comment /_static/manifests/com.apple.systempolicy.rule manifest.plist
.. pfmkey:: Expiration /_static/manifests/com.apple.systempolicy.rule manifest.plist
.. pfmkey:: OperationType /_static/manifests/com.apple.systempolicy.rule manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW22>`_.
