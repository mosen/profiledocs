.. _payloadtype-com.apple.webcontent-filter:

Web Content Filter
==================
:download:`Template <../_static/examples/com.apple.webcontent-filter.mobileconfig>`

The Web Content Filter payload allows you to whitelist and blacklist specific web URLs. This payload is supported only on supervised devices.

When multiple content filter payloads are present:

- The blacklist is the union of all blacklists—that is, any URL that appears in any blacklist is inaccessible.
- The permitted list is the intersection of all permitted lists—that is, only URLs that appear in every permitted list
  are accessible when they would otherwise be blocked by the automatic filter.
- The whitelist list is the intersection of all whitelists—that is, only URLs that appear in every whitelist are accessible.
- URLs are matched by using string-based root matching. A URL matches a whitelist, blacklist, or permitted list pattern
  if the exact characters of the pattern appear as the root of the URL.

  For example, if test.com/a is blacklisted, then test.com, test.com/b, and test.com/c/d/e will all be blocked.
  Matching does not discard subdomain prefixes, so if test.com/a is blacklisted, m.test.com is not blocked.

  Also, no attempt is made to match aliases (IP address versus DNS names, for example) or to handle requests
  with explicit port numbers.

If a profile does not contain an array for PermittedURLs or WhitelistedBookmarks,
that profile is skipped when evaluating the missing array or arrays.

As an exception, if a payload contains an AutoFilterEnabled key, but does not contain a PermittedURLs array,
that profile is treated as containing an empty array—that is, all websites are blocked.

All filtering options are active simultaneously. Only URLs and sites that pass all rules are permitted.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.webcontent-filter manifest.plist

Keys
----

.. pfmkey:: FilterType /_static/manifests/com.apple.webcontent-filter manifest.plist

.. note:: FilterType must be **Plugin** on macOS

FilterType is BuiltIn
^^^^^^^^^^^^^^^^^^^^^

.. pfmkey:: AutoFilterEnabled /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: PermittedURLs /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: WhitelistedBookmarks /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: BlacklistedURLs /_static/manifests/com.apple.webcontent-filter manifest.plist

FilterType is Plugin
^^^^^^^^^^^^^^^^^^^^

.. pfmkey:: UserDefinedName /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: PluginBundleID /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: ServerAddress /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: UserName /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: Password /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: PayloadCertificateUUID /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: Organization /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: FilterBrowsers /_static/manifests/com.apple.webcontent-filter manifest.plist
.. pfmkey:: FilterSockets /_static/manifests/com.apple.webcontent-filter manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW45>`_.
