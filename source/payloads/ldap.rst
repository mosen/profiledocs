LDAP Account
============

An LDAP payload provides information about an LDAP server to use, including account information if required,
and a set of LDAP search policies to use when querying that LDAP server.

.. pfm:: com.apple.ldap.account manifest.plist

Keys
----

.. pfmkey:: LDAPAccountDescription com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPAccountUserName com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPAccountPassword com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPAccountHostName com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPAccountUseSSL com.apple.ldap.account manifest.plist
.. pfmkey:: LDAPSearchSettings com.apple.ldap.account manifest.plist
.. pfmkey:: CommunicationServiceRules com.apple.ldap.account manifest.plist