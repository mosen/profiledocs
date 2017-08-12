Post Composite Steps
====================

After MCXCompositor has written out a collection of preferences into ``/Library/Managed Preferences``, some of those
plist files will not contain directly usable preferences.

In the post composite step, intermediate plist files are read in order to take some kind of action, eg. create a Mail
account or substitute some variables inside the original plist.

.. note:: Mostly older payloads are affected by post composite steps.

Post composition is implemented in **[MCX_PostComposite]**

- postCompositeAppItems
- postCompositeBackup
- postCompositeBluetooth
- postCompositeByHost
- postCompositeDockStuff
- postCompositeEnergySaverStuff
- postCompositeGuestAccount
- postCompositeMacBuddy
- postCompositeLoginwindow
- postCompositeDiagnostics
- postCompositeMCXScripts
- postCompositeMCXRedirector
- postCompositeSafari
- postCompositeiChat
- postCompositeiCal
- postCompositeKerberos
- postCompositeMail
- postCompositeSharing
- postCompositeSidebar
- postCompositeRestrictions
- postCompositeTimeZone
- postCompositeUniversalAccessStuff
- postCompositeVPN
- postCompositeAirPort
- postCompositeMCXPrefs
- postCompositeScreensaver
- postCompositeSystemUIServer
