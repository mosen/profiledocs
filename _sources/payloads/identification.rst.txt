.. _payloadtype-com.apple.configurationprofile.identification:

Identification
==============
:download:`Template <../_static/examples/com.apple.configurationprofile.identification.mobileconfig>`

This payload allows you to save names of the account user and prompt text. If left blank, the user has to provide this information when he or she installs the profile.

The Identification payload is not supported in iOS.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.configurationprofile.identification manifest.plist
.. pfm:: manifests/manual/com.apple.configurationprofile.identification manifest.plist

Keys
----

.. pfmkey:: FullName manifests/manual/com.apple.configurationprofile.identification manifest.plist
.. pfmkey:: EmailAddress manifests/manual/com.apple.configurationprofile.identification manifest.plist
.. pfmkey:: UserName manifests/manual/com.apple.configurationprofile.identification manifest.plist
.. pfmkey:: Password manifests/manual/com.apple.configurationprofile.identification manifest.plist
.. pfmkey:: Prompt manifests/manual/com.apple.configurationprofile.identification manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW10>`_.
