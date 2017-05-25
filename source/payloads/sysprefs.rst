.. _payloadtype-com.apple.systempreferences:

System Preference Panes
=======================

System preferences panes may be Whitelisted (via ``EnabledPreferencePanes``) or Blacklisted
(via ``DisabledPreferencePanes``) using this payload.

.. warning:: This has been copied verbatim from MCX and the keys will need to be verified.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.systempreferences manifest.plist
.. pfm:: manifests/manual/com.apple.systempreferences manifest.plist

Bugs
----

- Samuel discussed a `bypass mechanism at AFP548 <https://www.afp548.com/2013/12/16/system-preferences-profiles-in-mavericks-plus-a-security-hole/>`_
  involving Customize/View. You should be aware that this restriction can be bypassed.
