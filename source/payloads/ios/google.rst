.. _payloadtype-com.apple.google-oauth:

Google Account Payload
======================

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.google-oauth.png
    :align: right
    :figwidth: 200px

:download:`Template </_static/examples/com.apple.google-oauth.mobileconfig>`

You can install multiple Google payloads.

Each Google payload sets up a Google email address as well as any other Google services the user enables after authentication.
Google accounts must be installed via MDM or by Apple Configurator 2 (if the device is supervised).

The payload never contains credentials; the user will be prompted to enter credentials shortly after the
payload has been successfully installed.

.. contents::

Summary
-------

.. pfmheader:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.google-oauth.plist

Keys
----

.. pfmkey:: AccountDescription /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.google-oauth.plist
.. pfmkey:: AccountName /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.google-oauth.plist
.. pfmkey:: EmailAddress /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.google-oauth.plist
.. pfmkey:: CommunicationServiceRules /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.google-oauth.plist
