.. _payloadtype-com.apple.dock:

Dock
====

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.dock.png
    :align: right
    :figwidth: 200px

:download:`Template </_static/examples/com.apple.dock.mobileconfig>`

The Dock payload is supported on the user channel and, except for AllowDockFixupOverride, on all version of macOS.
The key ``AllowDockFixupOverride`` is supported on macOS 10.12 and later. The key ``show-recents`` is supported on macOS 10.14 and later.

.. contents::

Summary
-------

.. pfmheader:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist

Keys
----

.. pfmkey:: orientation /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: position-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: autohide /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: autohide-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: minimize-to-application /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: minimize-to-application-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: magnification /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: magnify-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: largesize /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: magsize-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: show-process-indicators /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: show-recents /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: launchanim /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: launchanim-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: mineffect /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: mineffect-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: tilesize /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: size-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist

MCXDockSpecialFolders can contain any of the valid mcxfolderflag values
.. pfmkey:: MCXDockSpecialFolders:mcxfolderflag /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist

.. pfmkey:: AllowDockFixupOverride /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist

.. pfmkey:: static-only /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
.. pfmkey:: static-others /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist

Each item in static-others is a dictionary containing the following keys:

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
    :key: static-others:doctile

**tile-data**

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
    :key: static-others:doctile:tile-data

**file-data**

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
    :key: static-others:doctile:tile-data:file-data

**url**

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
    :key: static-others:doctile:tile-data:url

.. pfmkey:: static-apps /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist

Each item in static-apps is a dictionary containing the following keys:

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
    :key: static-apps:apptile

**tile-data**

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
    :key: static-apps:apptile:tile-data

**file-data**

.. pfm:: /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist
    :key: static-apps:apptile:tile-data:file-data

.. pfmkey:: contents-immutable /_static/ProfileManifests/Manifests/ManifestsApple/com.apple.dock.plist


