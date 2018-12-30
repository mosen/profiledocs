.. _payloadtype-com.apple.assetcache.client.osx.profile.plugin:

AssetCache Client
=================
:download:`Template </_static/examples/com.apple.assetcache.client.osx.profile.plugin.mobileconfig>`

.. note:: TODO Key functionality still needs verification

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.assetcache.client.osx.profile.plugin manifest.plist

Multiple Payloads
-----------------

AssetCacheLocator XPC Service reads multiple entries from :path:`/Library/Preferences/com.apple.AssetCacheClientProfiles.plist`
so it seems at first glance that multiple *PublicIPAddressRange* keys will all be considered in sequence.
