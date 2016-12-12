LDAP Account
============

An LDAP payload provides information about an LDAP server to use, including account information if required,
and a set of LDAP search policies to use when querying that LDAP server.

.. pfm:: manifests/ac2/com.apple.ldap.account manifest.plist

Keys
----

.. pfmkey:: LDAPAccountDescription manifests/ac2/com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPAccountUserName manifests/ac2/com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPAccountPassword manifests/ac2/com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPAccountHostName manifests/ac2/com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPAccountUseSSL manifests/ac2/com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPSearchSettings manifests/ac2/com.apple.ldap.account manifest.plist
.. pfmkey:: CommunicationServiceRules manifests/ac2/com.apple.ldap.account manifest.plist