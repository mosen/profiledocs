mdmclient
=========

The ``mdmclient`` binary ships with the operating system and is located in ``/usr/libexec/mdmclient``.

Several subcommands are available, some related to troubleshooting MDM.

- airplay
- agent
- cleanconfigprofile
- cloudconfig
- daemon
- dep
- dep nag
- dumpSCEPVars
- encrypt
- installedProfiles
- InstallSystemProfile
- InstallUserProfile
- logevents
- mcx_userlogin
- MDMSim
- mdmsim
- nop
- preLoginCheckin
- QueryAppInstallation
- QueryCertificates
- QueryDeviceInformation
- QueryInstalledApps
- QueryInstalledProfiles
- QueryNetworkInformation
- QuerySecurityInfo
- removeSystemProfile
- removeUserProfile
- rundaemon
- stripCMS
- test
- testFDEKeyRotation
- testNSXPC

Common Flags
------------

``-debug``
    Debug mode

``-beepOnError``
    Beep on error

Commands for simulating MDM
---------------------------

airplay
^^^^^^^

Usage::

    /usr/libexec/mdmclient airplay start
    /usr/libexec/mdmclient airplay stop

Requires a plist containing a **RequestMirroring** payload for start, and a **StopMirroring** payload for stop.

QueryAppInstallation
^^^^^^^^^^^^^^^^^^^^

Usage::

    /usr/libexec/mdmclient QueryAppInstallation

Return information that would normally be returned to the MDM in a ``DeviceInformation`` query for Table 6 in

- `Official: DeviceInformation <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW15>`_.

QueryCertificates
^^^^^^^^^^^^^^^^^

Usage::

    /usr/libexec/mdmclient QueryCertificates

Return information that would normally be returned to the MDM in a ``CertificateList`` query.

- `Official: CertificateList <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW13>`_.

QueryDeviceInformation
^^^^^^^^^^^^^^^^^^^^^^

Usage::

    /usr/libexec/mdmclient QueryDeviceInformation

Return information that would normally be returned to the MDM in a ``DeviceInformation`` query for Table 7

- `Official: DeviceInformation - Table 7 <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW15>`_.

QueryInstalledApps
^^^^^^^^^^^^^^^^^^

Usage::

    /usr/libexec/mdmclient QueryInstalledApps

Return information that would normally be returned to the MDM in a ``InstalledApplicationList`` query.

- `Official: InstalledApplicationList <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW14>`_.

QueryInstalledProfiles
^^^^^^^^^^^^^^^^^^^^^^

Usage::

    /usr/libexec/mdmclient QueryInstalledProfiles

Return information that would normally be returned to the MDM in a ``ProfileList`` query.

- `Official: ProfileList <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW7>`_.

QueryNetworkInformation
^^^^^^^^^^^^^^^^^^^^^^^

Usage::

     /usr/libexec/mdmclient QueryNetworkInformation

Return information that would normally be returned to the MDM in a ``DeviceInformation`` query for Table 9

- `Official: DeviceInformation - Table 9 <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW15>`_.

QuerySecurityInfo
^^^^^^^^^^^^^^^^^

Usage::

     /usr/libexec/mdmclient QuerySecurityInfo

Return information that would normally be returned to the MDM in a ``SecurityInfo`` query.

- `Official: SecurityInfo <https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/3-MDM_Protocol/MDM_Protocol.html#//apple_ref/doc/uid/TP40017387-CH3-SW19>`_.

Commands for simulating DEP
---------------------------

dep nag
^^^^^^^

Usage::

     /usr/libexec/mdmclient dep nag

Clears out the cloud config activation record and retrieves a new one.

Basic sequence of events:

#. Previously saved profile at ``/var/db/ConfigurationProfiles/.cloudConfigProfileInstalled`` is deleted.
#. Tries to fetch a new cloud config profile.
#. If this succeeded it writes out ``/var/db/ConfigurationProfiles/.cloudConfigRecordFound``. If failed it writes
    ``/var/db/ConfigurationProfiles/.cloudConfigRecordNotFound`` instead (No DEP record for this device).

Misc debugging and utility commands
-----------------------------------

agent
^^^^^

Start XPC service ``com.apple.mdmclient.agent``.

dumpSessions (Unverified)
^^^^^^^^^^^^^^^^^^^^^^^^^

Outputs ``Debug mode enabled``.
Assume it logs communications with the MDM(?)

encrypt
^^^^^^^

Usage::

    /usr/libexec/mdmclient encrypt <recipient cert name> <path to plist>

Encrypt a payload into an encrypted payload.

dumpSCEPVars
^^^^^^^^^^^^

This command will show you what the substitution variable values for the SCEP payload will be.

mdmsim (Unverified)
^^^^^^^^^^^^^^^^^^^

Some kind of simulator although it is not known how to set this up.

Unverified commands
-------------------

testNSXPC
^^^^^^^^^

Actually seems to do nothing.

mcx_userlogin
^^^^^^^^^^^^^

Takes a plist from STDIN.

rundaemon
^^^^^^^^^

Used for the ``com.apple.mdmclient.daemon.runatboot`` launchd service.

installedProfiles
^^^^^^^^^^^^^^^^^

Similar to ``QueryInstalledProfiles`` but takes a **System** or **User** scope option.


