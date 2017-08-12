.. _payloadtype-com.apple.system.logging:

Unified Logging
===============

The unified logging payload allows you to configure logging levels by Subsystem (bundle ID), Process or for the System
as a whole. It also allows you to configure a different log level for persistent logs.

Also see the :manpage:`log(1)` man page for more information about the configuration.

Keys correspond to the directories under ``/Library/Preferences/Logging``.

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.system.logging manifest.plist
.. pfm:: /_static/manifests/com.apple.system.logging manifest.plist

Keys
----

.. note:: Only the keys for Subsystems are shown because the other types adhere to the same structure.

.. pfmkey:: Subsystems /_static/manifests/com.apple.system.logging manifest.plist

This dict contains one key by default called ``DEFAULT-OPTIONS`` which is applied when no logging category is matched.
The format of this dict is as below:

Default Options
^^^^^^^^^^^^^^^

.. pfm:: /_static/manifests/com.apple.system.logging manifest.plist
    :key: Subsystems:subsystemDomain:DEFAULT-OPTIONS

.. pfmkey:: Subsystems:subsystemDomain:DEFAULT-OPTIONS:Level /_static/manifests/com.apple.system.logging manifest.plist
.. pfm:: /_static/manifests/com.apple.system.logging manifest.plist
    :key: Subsystems:subsystemDomain:DEFAULT-OPTIONS:Level

.. pfmkey:: Subsystems:subsystemDomain:DEFAULT-OPTIONS:Default-Privacy-Setting /_static/manifests/com.apple.system.logging manifest.plist

.. pfmkey:: Subsystems:subsystemDomain:DEFAULT-OPTIONS:TTL /_static/manifests/com.apple.system.logging manifest.plist
.. pfm:: /_static/manifests/com.apple.system.logging manifest.plist
    :key: Subsystems:subsystemDomain:DEFAULT-OPTIONS:TTL

.. pfmkey:: Subsystems:subsystemDomain:DEFAULT-OPTIONS:Propagate-with-Activity /_static/manifests/com.apple.system.logging manifest.plist

.. pfmkey:: Subsystems:CategoryName /_static/manifests/com.apple.system.logging manifest.plist

.. pfmkey:: Subsystems:Enable-Oversize-Messages /_static/manifests/com.apple.system.logging manifest.plist

Notes
-----

- Profile install/remove is done in ``/System/Library/PrivateFrameworks/LoggingSupport.framework`` not the PDP.

Links
-----
