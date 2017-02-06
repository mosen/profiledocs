Dock
====

The Dock payload is supported on the user channel and, except for AllowDockFixupOverride, on all version of macOS.
The key ``AllowDockFixupOverride`` is supported on macOS 10.12 and later.

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.dock manifest.plist
.. pfm:: /_static/manifests/com.apple.dock manifest.plist

Keys
----

.. pfmkey:: orientation /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: position-immutable /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: autohide /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: autohide-immutable /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: minimize-to-application /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: minimize-to-application-immutable /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: magnification /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: magnify-immutable /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: largesize /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: magsize-immutable /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: show-process-indicators /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: launchanim /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: launchanim-immutable /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: mineffect /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: mineffect-immutable /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: tilesize /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: size-immutable /_static/manifests/com.apple.dock manifest.plist

MCXDockSpecialFolders can contain any of the valid mcxfolderflag values
.. pfmkey:: MCXDockSpecialFolders:mcxfolderflag /_static/manifests/com.apple.dock manifest.plist

.. pfmkey:: AllowDockFixupOverride /_static/manifests/com.apple.dock manifest.plist

.. pfmkey:: static-only /_static/manifests/com.apple.dock manifest.plist
.. pfmkey:: static-others /_static/manifests/com.apple.dock manifest.plist

Each item in static-others is a dictionary containing the following keys:

.. pfm:: /_static/manifests/com.apple.dock manifest.plist
    :key: static-others:doctile

**tile-data**

.. pfm:: /_static/manifests/com.apple.dock manifest.plist
    :key: static-others:doctile:tile-data

**file-data**

.. pfm:: /_static/manifests/com.apple.dock manifest.plist
    :key: static-others:doctile:tile-data:file-data

**url**

.. pfm:: /_static/manifests/com.apple.dock manifest.plist
    :key: static-others:doctile:tile-data:url

.. pfmkey:: static-apps /_static/manifests/com.apple.dock manifest.plist

Each item in static-apps is a dictionary containing the following keys:

.. pfm:: /_static/manifests/com.apple.dock manifest.plist
    :key: static-apps:apptile

**tile-data**

.. pfm:: /_static/manifests/com.apple.dock manifest.plist
    :key: static-apps:apptile:tile-data

**file-data**

.. pfm:: /_static/manifests/com.apple.dock manifest.plist
    :key: static-apps:apptile:tile-data:file-data

.. pfmkey:: contents-immutable /_static/manifests/com.apple.dock manifest.plist

