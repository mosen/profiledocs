InstallApplication
==================

Caveats
-------

- It is impossible to know whether the installation succeeded or failed.


OS Specific Notes
-----------------

10.12.0 - 10.12.3
^^^^^^^^^^^^^^^^^

- **InstallApplication** will not work before you send a response to ``AwaitDeviceConfiguration``.

10.11.x
^^^^^^^

- **InstallApplication** only works if there is a currently logged in user session.


Links
-----

- `Official Documentation <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW52>`_.
