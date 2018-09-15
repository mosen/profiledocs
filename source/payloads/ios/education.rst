.. _payloadtype-com.apple.education:

Education Payload
=================
:download:`Template <../_static/examples/com.apple.education.mobileconfig>`

The Education Configuration Payload defines the users, groups, and departments within an educational organization.

- All identities must be configured as both SSL clients and servers.
- Leader certificates must have the common name prefix "leader" (case insensitive).
- Member certificates must have the common name prefix "member" (case insensitive).

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.education manifest.plist

Keys
----

.. pfmkey:: OrganizationUUID /_static/manifests/com.apple.education manifest.plist
.. pfmkey:: OrganizationName /_static/manifests/com.apple.education manifest.plist
.. pfmkey:: PayloadCertificateUUID /_static/manifests/com.apple.education manifest.plist
.. pfmkey:: LeaderPayloadCertificateAnchorUUID /_static/manifests/com.apple.education manifest.plist
.. pfmkey:: MemberPayloadCertificateAnchorUUID /_static/manifests/com.apple.education manifest.plist
.. pfmkey:: UserIdentifier /_static/manifests/com.apple.education manifest.plist
.. pfmkey:: Departments /_static/manifests/com.apple.education manifest.plist

Department Items
^^^^^^^^^^^^^^^^

.. pfm:: /_static/manifests/com.apple.education manifest.plist
    :key: Departments:DepartmentItem

.. pfmkey:: Groups /_static/manifests/com.apple.education manifest.plist

Group Items
^^^^^^^^^^^

.. pfm:: /_static/manifests/com.apple.education manifest.plist
    :key: Groups:GroupItem

.. pfmkey:: Users /_static/manifests/com.apple.education manifest.plist

User Items
^^^^^^^^^^
.. pfm:: /_static/manifests/com.apple.education manifest.plist
    :key: Users:UserItem


.. pfmkey:: DeviceGroups /_static/manifests/com.apple.education manifest.plist

.. pfm:: /_static/manifests/com.apple.education manifest.plist
    :key: DeviceGroups:DeviceGroupItem


Links
-----

- `Official Documentation <https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1-SW601>`_.
