Dock
====

.. warning:: These manifest keys have been imported from MCX, they have not yet been verified.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.dock manifest.plist
.. pfm:: manifests/manual/com.apple.dock manifest.plist

Keys
----

.. pfmkey:: autohide manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: launchanim manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: magnify manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: mineffect manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: orientation manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: show-process-indicators manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: AllowDockFixupOverride manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: tilesize manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: static-only manifests/manual/com.apple.dock manifest.plist
.. pfmkey:: static-apps manifests/manual/com.apple.dock manifest.plist

Each item in static-apps is a dictionary containing the following keys:

.. pfm:: manifests/manual/com.apple.dock manifest.plist
    :key: AppItems-Raw:apptile

**tile-data**

.. pfm:: manifests/manual/com.apple.dock manifest.plist
    :key: AppItems-Raw:apptile:tile-data

**file-data**

.. pfm:: manifests/manual/com.apple.dock manifest.plist
    :key: AppItems-Raw:apptile:tile-data:file-data


.. pfmkey:: static-others manifests/manual/com.apple.dock manifest.plist

Each item in static-others is a dictionary containing the following keys:

.. pfm:: manifests/manual/com.apple.dock manifest.plist
    :key: DocItems-Raw:doctile

**tile-data**

.. pfm:: manifests/manual/com.apple.dock manifest.plist
    :key: DocItems-Raw:doctile:tile-data

**file-data**

.. pfm:: manifests/manual/com.apple.dock manifest.plist
    :key: DocItems-Raw:doctile:tile-data:file-data

**url**

.. pfm:: manifests/manual/com.apple.dock manifest.plist
    :key: DocItems-Raw:doctile:tile-data:url


.. pfmkey:: MCXDockSpecialFolders manifests/manual/com.apple.dock manifest.plist

MCXDockSpecialFolders can contain any of the valid mcxfolderflag values

.. pfmkey:: MCXDockSpecialFolders:mcxfolderflag manifests/manual/com.apple.dock manifest.plist