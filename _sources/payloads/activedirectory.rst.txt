.. _payloadtype-com.apple.DirectoryService.managed:

Active Directory
================
:download:`Template <../_static/examples/com.apple.DirectoryService.managed.mobileconfig>`

Join an active directory domain.

Advanced AD options available via Directory Utility or the dsconfigad command line tool can also be set using a configuration profile.

- ClientID does not appear in the official documentation.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.DirectoryService.managed manifest.plist

.. pfm:: manifests/manual/com.apple.DirectoryService.managed manifest.plist

Keys
----

.. pfmkey:: HostName manifests/manual/com.apple.DirectoryService.managed manifest.plist

.. note:: Apple documentation says the domain name, Profile Manager refers to a domain controller hostname.

.. pfmkey:: UserName manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: Password manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ClientID manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADOrganizationalUnit manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADCreateMobileAccountAtLoginFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADCreateMobileAccountAtLogin manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADWarnUserBeforeCreatingMAFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADWarnUserBeforeCreatingMA manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADForceHomeLocalFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADForceHomeLocal manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADUseWindowsUNCPathFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADUseWindowsUNCPath manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMountStyle manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADDefaultUserShellFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADDefaultUserShell manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapUIDAttributeFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapUIDAttribute manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapGIDAttributeFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapGIDAttribute manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapGGIDAttributeFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapGGIDAttribute manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPreferredDCServerFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPreferredDCServer manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADDomainAdminGroupListFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADDomainAdminGroupList manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADAllowMultiDomainAuthFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADAllowMultiDomainAuth manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADNamespaceFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADNamespace manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPacketSignFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPacketSign manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPacketEncryptFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPacketEncrypt manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADRestrictDDNSFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADRestrictDDNS manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADTrustChangePassIntervalDaysFlag manifests/manual/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADTrustChangePassIntervalDays manifests/manual/com.apple.DirectoryService.managed manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW62>`_.