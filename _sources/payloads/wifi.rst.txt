Wi-Fi
=====

.. warning:: The profile cannot be installed if your machine does not have a Wi-Fi AirPort adapter. USB Adapters do not
    qualify, so you may have issues testing in a Virtual Machine. This is because it uses CoreWLAN to make the settings
    and CoreWLAN will only return AirPort devices.

Summary
-------

.. pfmheader:: manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfm:: manifests/ac2/com.apple.wifi.managed manifest.plist

Keys
----

.. pfmkey:: SSID_STR manifests/ac2/com.apple.wifi.managed manifest.plist

- In iOS 7.0 and later, this is optional if a DomainName value is provided

.. pfmkey:: HIDDEN_NETWORK manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: AutoJoin manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 5.0 and later and in all versions of macOS.

.. pfmkey:: CaptiveBypass manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 10.0 and later.

.. pfmkey:: EncryptionType manifests/ac2/com.apple.wifi.managed manifest.plist

- Key available in iOS 4.0 and later and in all versions of macOS. The None value is available in iOS 5.0 and later and the WPA2 value is available in iOS 8.0 and later.

.. pfmkey:: IsHotspot manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 7.0 and later and in macOS 10.9 and later.

.. pfmkey:: DomainName manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 7.0 and later and in macOS 10.9 and later.

.. pfmkey:: DisplayedOperatorName manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 7.0 and later and in macOS 10.9 and later.

.. pfmkey:: ServiceProviderRoamingEnabled manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 7.0 and later and in macOS 10.9 and later.

.. pfmkey:: RoamingConsortiumOIs manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 7.0 and later and in macOS 10.9 and later.

.. pfmkey:: NAIRealmNames manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 7.0 and later and in macOS 10.9 and later.

.. pfmkey:: MCCAndMNCs manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 7.0 and later. This feature is not supported in macOS.

.. pfmkey:: EAPClientConfiguration manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: Password manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: PayloadCertificateUUID manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: TLSCertificateRequired manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyType manifests/ac2/com.apple.wifi.managed manifest.plist

- Available in iOS 5.0 and later and on all versions of macOS.

.. pfmkey:: ProxyServer manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyUsername manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyServerPort manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyPassword manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyPACURL manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyPACFallbackAllowed manifests/ac2/com.apple.wifi.managed manifest.plist
.. pfmkey:: QoSMarkingPolicy manifests/ac2/com.apple.wifi.managed manifest.plist

Available in iOS 10.0 and later. Not supported in macOS.