Logging
=======

There are several different processes related to profile installation and MDM command acknowledgement.
The easiest option is to download this :download:`Logging Profile </_static/profiles/MDM Debug Logging.mobileconfig>`
for macOS 10.12 and higher.


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

.. note:: Some parts of ManagedClient don't use Unified Logging so you'll probably need to enable this also.

Log Location
    /Library/Logs/ManagedClient/ManagedClient.log


Commands::

    sudo defaults write /Library/Preferences/com.apple.MCXDebug debugOutput -2
    sudo defaults write /Library/Preferences/com.apple.MCXDebug collateLogs 1


Unified Logging Predicates
--------------------------

Various predicates can be directly entered into the *Console.app* and saved.

.. note:: Sometimes if you search by process name, you get a lot of noise. Example: searching for **mdmclient** forces
    you to wade through a ton of push service notifications.

Some useful predicates:

- ``subsystem:com.apple.ManagedClient`` Messages in this category cover a broad range of profile installation messages.
- ``subsystem:com.apple.securityd`` Interactions with the keychain
- ``category:SCEP.fw`` SCEP network requests only (no warnings on signature verification etc).

Payload specific combinations:

- ``subsystem:com.apple.ManagedClient library:Certificate`` Certificate payload messages

