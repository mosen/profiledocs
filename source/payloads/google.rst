Google Account
==============

You can install multiple Google payloads.

Each Google payload sets up a Google email address as well as any other Google services the user enables after authentication.
Google accounts must be installed via MDM or by Apple Configurator 2 (if the device is supervised).

The payload never contains credentials; the user will be prompted to enter credentials shortly after the
payload has been successfully installed.

.. pfm:: com.apple.google-oauth manifest.plist

Keys
----

.. pfmkey:: AccountDescription com.apple.google-oauth manifest.plist
.. pfmkey:: AccountName com.apple.google-oauth manifest.plist
.. pfmkey:: EmailAddress com.apple.google-oauth manifest.plist
