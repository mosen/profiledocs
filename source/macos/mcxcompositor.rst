MCXCompositor
=============

Location
    /System/Library/CoreServices/ManagedClient.app/Contents/Resources/MCXCompositor

Summary
-------

MCXCompositor takes the role of combining custom preferences into their preference domains, located within
``/Library/Managed Preferences``.

Flags
-----

``-w=/path/to/output``
    Output path

``-r=FilterKey``
    in ``/System/Library/CoreServices/ManagedClient.app/Contents/Resources/Compositor.plist`` there are lists of bundles
    to be excluded from composition. The filter key chooses one of those lists.

``-h=homedir``
    Home directory

``-s=shortname``
    Short name (per-user prefs are composited by short username)

``-p=/tmp``
    Unknown: May be temporary processing dir

``-I``
    Unknown: May be "read from STDIN"

``-i=<int>``
    Unknown: May be User UID

``-a``
    Unknown



Sequence
--------

- Remove contents of ``/Library/Managed Preferences``.
- Can call **_CFPreferencesWriteManagedDomainForUser_Internal** to write into the shortname directory there.

