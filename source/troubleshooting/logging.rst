Logging
=======

There are several different processes related to profile installation and MDM command acknowledgement.
The easiest option is to download this :download:`Logging Profile </_static/profiles/MDM Debug Logging.mobileconfig>`
for macOS 10.12 and higher.

Push Notifications
------------------

Log Location
    /Library/Logs/apsd.log

Commands::

    sudo touch /Library/Logs/apsd.log
    sudo defaults write /Library/Preferences/com.apple.apsd APSWriteLogs -bool TRUE
    sudo defaults write /Library/Preferences/com.apple.apsd APSLogLevel -int 7
    sudo killall apsd


Per Topic status can be retrieved by executing::

    /System/Library/PrivateFrameworks/ApplePushService.framework/apsctl status



MDM Debugging
-------------

Commands::

    sudo touch /var/db/MDM_EnableDebug


In macOS 10.12 you can configure the logging subsystem via a configuration profile (as above) or by using the :command:`log`
utility like so::

    sudo log config --subsystem com.apple.ManagedClient --mode="level:debug,persist:debug"

You will probably want to reset this back to normal so that debug logs are not persisted like so::

    sudo log config --subsystem com.apple.ManagedClient --reset
    


MCX
---

Log Location
    /Library/Logs/ManagedClient/ManagedClient.log


Commands::

    sudo defaults write /Library/Preferences/com.apple.MCXDebug debugOutput -2
    sudo defaults write /Library/Preferences/com.apple.MCXDebug collateLogs 1
