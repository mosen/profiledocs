.. _payloadtype-com.apple.firstactiveethernet.managed:

Ethernet 802.1x
===============
:download:`Template <../_static/examples/com.apple.firstactiveethernet.managed.mobileconfig>`

The 802.1x Ethernet payload is designated by specifying one of the following as the PayloadType value:

- com.apple.firstactiveethernet.managed [default]
- com.apple.firstethernet.managed
- com.apple.secondactiveethernet.managed
- com.apple.secondethernet.managed
- com.apple.thirdactiveethernet.managed
- com.apple.thirdethernet.managed

Payloads with **active** in their name apply to Ethernet interfaces that are working at the time of profile installation.
If there is no active Ethernet interface working, the ``com.apple.firstactiveethernet.managed`` payload will configure
the interface with the highest service order priority.

Payloads without **active** in the name apply to Ethernet interfaces according to service order regardless of whether
the interface is working or not.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.firstactiveethernet.managed manifest.plist
.. pfm:: manifests/manual/com.apple.firstactiveethernet.managed manifest.plist
