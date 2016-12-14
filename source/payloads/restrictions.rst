.. _payloadtype-com.apple.applicationaccess:

Restrictions
============

A Restrictions payload allows the administrator to restrict the user from doing certain things with the device, such as using the camera.

The Restrictions payload is supported in iOS; some keys are also supported in macOS, as noted below.

.. pfm:: manifests/manual/com.apple.applicationaccess manifest.plist

Keys
----

.. pfmkey:: allowAppInstallation manifests/manual/com.apple.applicationaccess manifest.plist

Supervised
    YES

.. tip:: This key is deprecated on unsupervised devices.

.. pfmkey:: allowUIAppInstallation manifests/manual/com.apple.applicationaccess manifest.plist

Supervised
    YES

iOS
    9.0+

.. pfmkey:: allowAutomaticAppDownloads manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAppRemoval manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEnterpriseAppTrust manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCamera manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowExplicitContent manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowScreenShot manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowRemoteScreenObservation manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowChat manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowBookstore manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowBookstoreErotica manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowMusicService manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowRadioService manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowSharedStream manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPassbookWhileLocked manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowUIConfigurationProfileInstallation manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowiTunes manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowNews manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowSafari manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowGameCenter manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAddingGameCenterFriends manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowBluetoothModification manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAppCellularDataModification manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowDeviceNameModification manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPasscodeModification manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowWallpaperModification manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEnablingRestrictions manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowGlobalBackgroundFetchWhenRoaming manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowManagedAppsCloudSync manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEnterpriseBookBackup manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEnterpriseBookMetadataSync manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowInAppPurchases manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowMultiplayerGaming manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowVideoConferencing manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowVoiceDialing manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceEncryptedBackup manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceWatchWristDetection manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPairedWatch manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowEraseContentAndSettings manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowSpotlightInternetResults manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCloudDocumentSync manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowUntrustedTLSPrompt manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowDiagnosticSubmission manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowDiagnosticSubmissionModification manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPhotoStream manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCloudPhotoLibrary manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowCloudBackup manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceITunesStorePasswordEntry manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: ratingApps manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: ratingMovies manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: ratingTVShows manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: ratingRegion manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariAcceptCookies manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariAllowAutoFill manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariAllowJavaScript manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariAllowPopups manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: safariForceFraudWarning manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAssistant manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAssistantWhileLocked manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceAssistantProfanityFilter manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowPredictiveKeyboard manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowKeyboardShortcuts manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowAutoCorrection manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowSpellCheck manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowDefinitionLookup manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowOpenFromUnmanagedToManaged manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowOpenFromManagedToUnmanaged manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: forceAirDropUnmanaged manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowActivityContinuation manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowFingerprintForUnlock manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowFingerprintModification manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: allowNotificationsModification manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: blacklistedAppBundleIDs manifests/manual/com.apple.applicationaccess manifest.plist
.. pfmkey:: whitelistedAppBundleIDs manifests/manual/com.apple.applicationaccess manifest.plist