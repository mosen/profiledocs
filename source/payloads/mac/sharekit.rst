.. _payloadtype-com.apple.ShareKitHelper:

ShareKit
========

It can contain only one payload. It is supported on the User Channel.
The ShareKit Payload specifies which ShareKit plugin can be accessed on client. Both allow and disallow lists can be specified.

The following plugin IDs are supported by this payload:

com.apple.share.AirDrop
    AirDrop
com.apple.share.Facebook
    Facebook
com.apple.share.Twitter
    Twitter
com.apple.share.Mail
    Mail
com.apple.share.Messages
    Messages
com.apple.share.Video
    Video Services
com.apple.share.addtoiphoto
    Photos
com.apple.share.addtoaperture
    Aperture
com.apple.share.readlater
    Reading List
com.apple.share.SinaWeibo
    Sina Weibo
com.apple.Notes.SharingExtension
    Notes
com.apple.reminders.RemindersShareExtension
    Reminders
com.apple.share.LinkedIn.post
    LinkedIn

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.ShareKitHelper manifest.plist

Keys
----

.. pfmkey:: SHKAllowedShareServices /_static/manifests/com.apple.ShareKitHelper manifest.plist
.. pfmkey:: SHKDeniedShareServices /_static/manifests/com.apple.ShareKitHelper manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW642>`_.

