.. _payloadtype-com.apple.security.scep:

SCEP
====

An SCEP payload automates the request of a client certificate from an SCEP server.

.. note:: GetCACaps is mentioned in the documentation but not included in this manifest.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.security.scep manifest.plist
.. pfm:: manifests/manual/com.apple.security.scep manifest.plist
    :key: PayloadContent

Keys
----

.. pfmkey:: PayloadContent:URL manifests/manual/com.apple.security.scep manifest.plist
.. pfmkey:: PayloadContent:Name manifests/manual/com.apple.security.scep manifest.plist

Optional. Any string that is understood by the SCEP server. For example, it could be a domain name like example.org.
If a certificate authority has multiple CA certificates this field can be used to distinguish which is required.

.. pfmkey:: PayloadContent:Subject manifests/manual/com.apple.security.scep manifest.plist

Optional. The representation of a X.500 name represented as an array of OID and value.
For example, /C=US/O=Apple Inc./CN=foo/1.2.5.3=bar, which would translate to:

    [ [ ["C", "US"] ], [ ["O", "Apple Inc."] ], ..., [ [ "1.2.5.3", "bar" ] ] ]

OIDs can be represented as dotted numbers, with shortcuts for country (C), locality (L), state (ST), organization (O), organizational unit (OU), and common name (CN).

.. pfmkey:: PayloadContent:Challenge manifests/manual/com.apple.security.scep manifest.plist
.. pfmkey:: PayloadContent:Keysize manifests/manual/com.apple.security.scep manifest.plist
.. pfmkey:: PayloadContent:CAFingerprint manifests/manual/com.apple.security.scep manifest.plist
.. pfmkey:: PayloadContent:KeyType manifests/manual/com.apple.security.scep manifest.plist
.. pfmkey:: PayloadContent:KeyUsage manifests/manual/com.apple.security.scep manifest.plist
.. pfmkey:: PayloadContent:SubjectAltName manifests/manual/com.apple.security.scep manifest.plist
.. pfmkey:: PayloadContent:Retries manifests/manual/com.apple.security.scep manifest.plist
.. pfmkey:: PayloadContent:RetryDelay manifests/manual/com.apple.security.scep manifest.plist

Substitution Variables
----------------------

The values of these can be obtained by running (in a Terminal window)::

    /usr/libexec/mdmclient dumpSCEPVars


``%AD_ComputerID%``
    computername$

``%AD_ComputerName%``
    computername

``%AD_Domain%``
    CONTOSO

``%AD_DomainForestName%``
    contoso.com

``%AD_DomainGUID%``
    <GUID value>

``%AD_DomainNameDNS%``
    contoso.com

``%AD_KerberosID%``
    computer$@AD.DOMAIN

``%ComputerName%``
    computer

``%HardwareUUID%``
    <Hardware unique UUID>

``%HostName%``
    computer.local

``%LocalHostName%``
    computername

``%MACAddress%``
    ethernet mac address

``%SerialNumber%``
    mac serial number

Unified Logging
---------------

SCEP Networking
^^^^^^^^^^^^^^^

:Console: ``subsystem:com.apple.SCEP``
:CLI: ``log show --info --debug --predicate 'subsystem == "com.apple.SCEP"' --last 1h``

Certificate Payload Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^

:Console: ``subsystem:com.apple.ManagedClient library:Certificate``
:CLI: ``log show --info --debug --predicate '(subsystem == "com.apple.ManagedClient") && (senderImagePath ENDSWITH "Certificate")' --last 1h``


Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW18>`_.
- `Certificate Renewal Behaviour <https://support.apple.com/en-us/HT204446>`_.
