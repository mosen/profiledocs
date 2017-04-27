.. _payloadtype-com.apple.wifi.managed:

Wi-Fi
=====

.. warning:: The profile cannot be installed if your machine does not have a Wi-Fi AirPort adapter. USB Adapters do not
    qualify, so you may have issues testing in a Virtual Machine. This is because it uses CoreWLAN to make the settings
    and CoreWLAN will only return AirPort devices.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.wifi.managed manifest.plist
.. pfm:: manifests/manual/com.apple.wifi.managed manifest.plist

Keys
----

.. pfmkey:: SSID_STR manifests/manual/com.apple.wifi.managed manifest.plist

- In iOS 7.0 and later, this is optional if a DomainName value is provided

.. pfmkey:: HIDDEN_NETWORK manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: AutoJoin manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: CaptiveBypass manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EncryptionType manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: Password manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: PayloadCertificateUUID manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: TLSCertificateRequired manifests/manual/com.apple.wifi.managed manifest.plist

Keys (HotSpot)
--------------

.. pfmkey:: IsHotspot manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: DomainName manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: DisplayedOperatorName manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: ServiceProviderRoamingEnabled manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: RoamingConsortiumOIs manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: NAIRealmNames manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: MCCAndMNCs manifests/manual/com.apple.wifi.managed manifest.plist

Keys (802.1x)
-------------

.. pfmkey:: EAPClientConfiguration manifests/manual/com.apple.wifi.managed manifest.plist
.. pfm:: manifests/manual/com.apple.wifi.managed manifest.plist
    :key: EAPClientConfiguration

.. pfmkey:: EAPClientConfiguration:AcceptEAPTypes manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:UserName manifests/manual/com.apple.wifi.managed manifest.plist


.. pfmkey:: EAPClientConfiguration:UserPassword manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:OneTimeUserPassword manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:PayloadCertificateAnchorUUID manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:TLSTrustedServerNames manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:TLSAllowTrustExceptions manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:TTLSInnerAuthentication manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:OuterIdentity manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:SystemModeCredentialsSource manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:EAPFASTUsePAC manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:EAPFASTProvisionPAC manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: EAPClientConfiguration:EAPFASTProvisionPACAnonymously manifests/manual/com.apple.wifi.managed manifest.plist

Keys (Proxy)
------------

.. pfmkey:: ProxyType manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyServer manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyUsername manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyServerPort manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyPassword manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyPACURL manifests/manual/com.apple.wifi.managed manifest.plist
.. pfmkey:: ProxyPACFallbackAllowed manifests/manual/com.apple.wifi.managed manifest.plist

Keys (QoS)
----------

.. pfmkey:: QoSMarkingPolicy manifests/manual/com.apple.wifi.managed manifest.plist

Available in iOS 10.0 and later. Not supported in macOS.

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW30>`_.
