.. _payloadtype-com.apple.security.FDERecoveryRedirect:

FileVault Recovery Key Redirect
===============================
:download:`Template </_static/examples/com.apple.security.FDERecoveryRedirect.mobileconfig>`

FileVault full-volume encryption (FDE) recovery keys are, by default, sent to Apple if the user requests it.
With this key, you can redirect those recovery keys to a corporate server.

FileVault Recovery Key Redirection payloads are designated by specifying ``com.apple.security.FDERecoveryRedirect``
as the PayloadType value. Only one payload of this type is allowed per system.

A site providing support for archiving the recovery key must implement its own HTTPS server.
The client issues a POST request to the server with XML data in the request body containing the recovery key
and serial number of the client computer.
The server must respond with XML data echoing the device's serial number and provide a RecordNumber,
which can be any data that locates the recovery key.

The SSL certificate chain of the server is evaluated by the client, which must trust it.
If needed, the configuration profile can include an additional certificate to set up a chain of trust.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.security.FDERecoveryRedirect manifest.plist

Keys
----

.. pfmkey:: RedirectURL /_static/manifests/com.apple.security.FDERecoveryRedirect manifest.plist

.. pfmkey:: EncryptCertPayloadUUID /_static/manifests/com.apple.security.FDERecoveryRedirect manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW842>`_.


