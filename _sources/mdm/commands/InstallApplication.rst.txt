InstallApplication
==================

Caveats (10.12)
---------------

- It is impossible to know whether the installation succeeded or failed.
- If storedownloadd fails, it blocks all further application installs `OpenRADAR <https://openradar.appspot.com/26517261>`_. courtesy of bruienne.


Simultaneous Downloads
----------------------

Groob writes:

An ``InstallApplication`` command consists of two parts. A manifest plist and a signed pkg that the manifest points to.
Once the MDM server queues an ``InstallApplication``, the mdmclient process will defer the download to storedownloadd which does the following:

#. Sends "Acknowledged" or "NotNow" to the MDM server.
#. Uses HTTP GET request to fetch the manifest.
#. Caches the manifest locally. future requests skip step 1 and use the local cache.
   (I haven't done any investigation into how the cache is invalidated, but that's not important here.

What's important is that there are two initial requests for a single InstallApplication command.
- uses HTTP GET request to download the .pkg
- installs the pkg.
We can observe this action in the logs::

    # client log
    2017-04-29 21:30:02.362540-0400 0x4f27     Default     0x0                  616    mdmclient: [com.apple.ManagedClient.InstallApplication] Scheduled InstallApplication from: https://dev.micromdm.io/repo/munkitools.plist
    2017-04-29 21:30:03.892894-0400 0x4f83     Default     0x0                  621    storedownloadd: (StoreFoundation) [com.apple.commerce.CKLegacy] ISStoreURLOperation: Starting URL operation with url=https://dev.micromdm.io/repo/munkitools.pkg / bagKey=(null)

    # server log
    10.0.0.1 - - [01/May/2017:15:34:58 +0000] "GET /repo/munkitools.plist HTTP/1.1" 200 754 "" "MacAppStore/2.2 (Macintosh; OS X 10.12.3;
    16D30) AppleWebKit/2602.4.8"
    10.0.0.1 - - [01/May/2017:15:34:59 +0000] "GET /repo/munkitools.pkg HTTP/1.1" 200 730798 "" "MacAppStore/2.2 (Macintosh; OS X 10.

The Problem:

Queueing one ``InstallApplication`` command before the previous one completes will most likely cause only one install to actually succeed.
Here's what I'm seeing in the logs::

    # acknowledged two scheduled IA commands
    connected udid=4A7A3EC2-6755-4113-A5AF-AC10574D953A type=InstallApplication, status=Acknowledged
    connected udid=4A7A3EC2-6755-4113-A5AF-AC10574D953A type=InstallApplication, status=Acknowledged

    #
    10.0.0.1 - - [01/May/2017:15:34:58 +0000] "GET /repo/package-A.plist HTTP/1.1" 200 758 "" "MacAppStore/2.2 (Macintosh; OS X 10.12.3; 16D30) AppleWebKit/2602.4.8"
    10.0.0.1 - - [01/May/2017:15:34:58 +0000] "GET /repo/package-B.plist HTTP/1.1" 200 754 "" "MacAppStore/2.2 (Macintosh; OS X 10.12.3; 16D30) AppleWebKit/2602.4.8"
    10.0.0.1 - - [01/May/2017:15:34:59 +0000] "GET /repo/package-A.pkg HTTP/1.1" 200 730798 "" "MacAppStore/2.2 (Macintosh; OS X 10.
    # and done. package-B.pkg is never downloaded.

The storedownloadd is scheduled to download two or more applications, but it ends up losing track of things and only downloads one.
This problem doesn't happen if both installs are being repeated and the plist is not being downloaded.
The problem also doesn't happen if the ``InstallApplication`` commands are spaced out such that the first install is completed before the second one starts.

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
- `MicroMDM Issue #151 groob <https://github.com/micromdm/micromdm/issues/151#issuecomment-298535040>`_.
