.. _vpn-ikev2:

IKEv2
=====

Summary
-------

.. pfmkey:: IKEv2 /_static/manifests/com.apple.vpn.managed manifest.plist

.. pfm:: /_static/manifests/com.apple.vpn.managed manifest.plist
    :key: IKEv2

Keys
----

.. pfmkey:: IKEv2:RemoteAddress /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:LocalIdentifier /_static/manifests/com.apple.vpn.managed manifest.plist

Identifier of the IKEv2 client in one of the following formats:

- FQDN
- UserFQDN
- Address
- ASN1DN

.. pfmkey:: IKEv2:RemoteIdentifier /_static/manifests/com.apple.vpn.managed manifest.plist

Identifier of the IKEv2 client in one of the following formats:

- FQDN
- UserFQDN
- Address
- ASN1DN

.. pfmkey:: IKEv2:AuthenticationMethod /_static/manifests/com.apple.vpn.managed manifest.plist

.. note::
    To enable EAP-only authentication, the authentication method should be set to *None* and the *ExtendedAuthEnabled* key
    should be set to 1. If this key is set to *None* and the *ExtendedAuthEnabled* key is not set, the authentication
    configuration defaults to *SharedSecret*.

.. pfmkey:: IKEv2:PayloadCertificateUUID /_static/manifests/com.apple.vpn.managed manifest.plist

If the value of AuthenticationMethod is Certificate, this certificate is sent out for IKEv2 machine authentication.
If extended authentication (EAP) is used, it is sent out for EAP-TLS authentication.

.. pfmkey:: IKEv2:SharedSecret /_static/manifests/com.apple.vpn.managed manifest.plist

If AuthenticationMethod is SharedSecret, this value is used for IKE authentication.

.. pfmkey:: IKEv2:ExtendedAuthEnabled /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:AuthName /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:DisableRedirect /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:DisableMOBIKE /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:UseConfigurationAttributeInternalIPSubnet /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:EnablePFS /_static/manifests/com.apple.vpn.managed manifest.plist

.. pfmkey:: IKEv2:ServerAddresses /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:SearchDomains /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:DomainName /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:SupplementalMatchDomains /_static/manifests/com.apple.vpn.managed manifest.plist

This key is used to create a split DNS configuration where only hosts in certain domains are resolved
using the tunnel’s DNS resolver. Hosts not in one of the domains in this list are resolved using the system’s default resolver.

If SupplementalMatchDomains contains the empty string it becomes the default domain.
This is how a split-tunnel configuration can direct all DNS queries first to the VPN DNS servers before
the primary DNS servers.

If the VPN tunnel becomes the network’s default route, the servers listed in *ServerAddresses* become the default
resolver and the *SupplementalMatchDomains* list is ignored.

.. pfmkey:: IKEv2:EnableCertificateRevocationCheck /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:AuthPassword /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:DeadPeerDetectionRate /_static/manifests/com.apple.vpn.managed manifest.plist

None
    Disabled

Low
    *keepalive* sent every 30 minutes

Medium
    *keepalive* sent every 10 minutes

High
    *keepalive* sent every 1 minute



.. pfmkey:: IKEv2:CertificateType /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfmkey:: IKEv2:ServerCertificateIssuerCommonName /_static/manifests/com.apple.vpn.managed manifest.plist

If set, this field will cause IKE to send a certificate request based on this certificate issuer to the server.

This key is required if both the CertificateType key is included and the ExtendedAuthEnabled key is set to 1.

.. pfmkey:: IKEv2:ServerCertificateCommonName /_static/manifests/com.apple.vpn.managed manifest.plist

This name is used to validate the certificate sent by the IKE server.
If not set, the Remote Identifier will be used to validate the certificate.

.. pfmkey:: IKEv2:NATKeepAliveOffloadEnable /_static/manifests/com.apple.vpn.managed manifest.plist

Keepalive packets are sent by the device to maintain NAT mappings for IKEv2 connections that have a NAT on the path.
Keepalive packets are sent at regular interval when the device is awake.
If *NATKeepAliveOffloadEnable* is set to 1, Keepalive packets will be offloaded to hardware while the device is asleep.
NAT Keepalive offload has an impact on the battery life since extra workload is added during sleep.
The default interval for the Keepalive offload packets is 20 seconds over WiFi and 110 seconds over Cellular interface.
The default NAT Keepalive works well on networks with small NAT mapping timeouts but imposes a potential battery impact.
If a network is known to have larger NAT mapping timeouts, larger Keepalive intervals may be safely used to minimize
battery impact.

The Keepalive interval can be modified by setting the *NATKeepAliveInterval* key.

.. pfmkey:: IKEv2:NATKeepAliveInterval /_static/manifests/com.apple.vpn.managed manifest.plist

This value controls the interval over which Keepalive offload packets are sent by the device.
The minimum value is 20 seconds.

If no key is specified, the default is 20 seconds over WiFi and 110 seconds over a Cellular interface.

.. pfmkey:: IKEv2:IKESecurityAssociationParameters /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfm:: /_static/manifests/com.apple.vpn.managed manifest.plist
    :key: IKEv2:IKESecurityAssociationParameters

.. pfmkey:: IKEv2:ChildSecurityAssociationParameters /_static/manifests/com.apple.vpn.managed manifest.plist
.. pfm:: /_static/manifests/com.apple.vpn.managed manifest.plist
    :key: IKEv2:ChildSecurityAssociationParameters
