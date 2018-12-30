.. _payloadtype-com.apple.DirectoryService.managed:

Active Directory
================
:download:`Template </_static/examples/com.apple.DirectoryService.managed.mobileconfig>`

Join an active directory domain.

Advanced AD options available via Directory Utility or the dsconfigad command line tool can also be set using a configuration profile.

- ClientID does not appear in the official documentation.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.DirectoryService.managed manifest.plist

Keys
----

.. pfmkey:: HostName /_static/manifests/com.apple.DirectoryService.managed manifest.plist

.. note:: Apple documentation says the domain name, Profile Manager refers to a domain controller hostname.

.. pfmkey:: UserName /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: Password /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ClientID /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADOrganizationalUnit /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADCreateMobileAccountAtLoginFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADCreateMobileAccountAtLogin /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADWarnUserBeforeCreatingMAFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADWarnUserBeforeCreatingMA /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADForceHomeLocalFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADForceHomeLocal /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADUseWindowsUNCPathFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADUseWindowsUNCPath /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMountStyle /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADDefaultUserShellFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADDefaultUserShell /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapUIDAttributeFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapUIDAttribute /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapGIDAttributeFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapGIDAttribute /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapGGIDAttributeFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADMapGGIDAttribute /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPreferredDCServerFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPreferredDCServer /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADDomainAdminGroupListFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADDomainAdminGroupList /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADAllowMultiDomainAuthFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADAllowMultiDomainAuth /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADNamespaceFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADNamespace /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPacketSignFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPacketSign /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPacketEncryptFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADPacketEncrypt /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADRestrictDDNSFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADRestrictDDNS /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADTrustChangePassIntervalDaysFlag /_static/manifests/com.apple.DirectoryService.managed manifest.plist
.. pfmkey:: ADTrustChangePassIntervalDays /_static/manifests/com.apple.DirectoryService.managed manifest.plist

Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW62>`_.