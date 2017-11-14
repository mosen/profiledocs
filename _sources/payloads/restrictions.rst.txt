.. _payloadtype-com.apple.applicationaccess:

Restrictions
============
:download:`Template <../_static/examples/com.apple.applicationaccess.mobileconfig>`

A Restrictions payload allows the administrator to restrict the user from doing certain things with the device, such as using the camera.

The Restrictions payload is supported in iOS; some keys are also supported in macOS, as noted below.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.applicationaccess manifest.plist

Keys
----

.. pfmkey:: allowAppInstallation /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowUIAppInstallation /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAutomaticAppDownloads /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAppRemoval /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEnterpriseAppTrust /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCamera /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowExplicitContent /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowScreenShot /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowRemoteScreenObservation /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowChat /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowBookstore /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowBookstoreErotica /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowMusicService /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowRadioService /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowSharedStream /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPassbookWhileLocked /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowUIConfigurationProfileInstallation /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowiTunes /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowNews /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowSafari /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowGameCenter /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAddingGameCenterFriends /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowBluetoothModification /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAppCellularDataModification /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowDeviceNameModification /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPasscodeModification /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowWallpaperModification /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEnablingRestrictions /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowGlobalBackgroundFetchWhenRoaming /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowManagedAppsCloudSync /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEnterpriseBookBackup /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEnterpriseBookMetadataSync /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowInAppPurchases /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowMultiplayerGaming /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowVideoConferencing /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowVoiceDialing /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceEncryptedBackup /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceWatchWristDetection /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPairedWatch /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEraseContentAndSettings /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowSpotlightInternetResults /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCloudDocumentSync /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowUntrustedTLSPrompt /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowDiagnosticSubmission /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowDiagnosticSubmissionModification /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPhotoStream /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCloudPhotoLibrary /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCloudBackup /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceITunesStorePasswordEntry /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: ratingApps /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: ratingMovies /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: ratingTVShows /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: ratingRegion /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariAcceptCookies /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariAllowAutoFill /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariAllowJavaScript /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariAllowPopups /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariForceFraudWarning /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAssistant /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAssistantWhileLocked /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceAssistantProfanityFilter /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPredictiveKeyboard /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowKeyboardShortcuts /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAutoCorrection /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowSpellCheck /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowDefinitionLookup /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowOpenFromUnmanagedToManaged /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowOpenFromManagedToUnmanaged /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceAirDropUnmanaged /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowActivityContinuation /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowFingerprintForUnlock /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowFingerprintModification /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowNotificationsModification /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: blacklistedAppBundleIDs /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: whitelistedAppBundleIDs /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAutoUnlock /_static/manifests/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCloudDesktopAndDocuments /_static/manifests/com.apple.applicationaccess manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW13>`_.
