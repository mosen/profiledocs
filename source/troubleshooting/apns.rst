APNS (Push Notifications)
=========================

apsctl
------

Location
    /System/Library/PrivateFrameworks/ApplePushService.framework/apsctl

You may run ``apsctl status`` to see the status of all APNS topics on the local machine.
Regarding MDM, you are looking at these topics:

- com.apple.mdmclient.agent.push.production (User Channel)
- com.apple.mdmclient.daemon.push.production (Device Channel)

Example::

    /System/Library/PrivateFrameworks/ApplePushService.framework/apsctl status |grep -A 25 com.apple.mdmclient.daemon.push.production

Should show you roughly all the relevant lines from the apns topic for mdmclient.

From this information you can learn about:

- The last time the device received a push notification for MDM.
- The last topic that was used to receive a push notification.
- The number of push notifications received.
- etc.


