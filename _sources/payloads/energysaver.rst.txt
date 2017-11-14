.. _payloadtype-com.apple.MCX:

Energy Saver
============
:download:`Template <../_static/examples/com.apple.MCX.mobileconfig>`

This payload describes Energy Saver / Power Management settings.
For more information on the individual settings you can also consult the :command:`pmset(1)` tool.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.MCX manifest.plist

Keys
----

.. pfmkey:: DestroyFVKeyOnStandby /_static/manifests/com.apple.MCX manifest.plist
.. pfmkey:: SleepDisabled /_static/manifests/com.apple.MCX manifest.plist
.. pfmkey:: com.apple.EnergySaver.desktop.ACPower-ProfileNumber /_static/manifests/com.apple.MCX manifest.plist
.. pfmkey:: com.apple.EnergySaver.portable.ACPower-ProfileNumber /_static/manifests/com.apple.MCX manifest.plist
.. pfmkey:: com.apple.EnergySaver.portable.BatteryPower-ProfileNumber /_static/manifests/com.apple.MCX manifest.plist
.. pfmkey:: com.apple.EnergySaver.desktop.ACPower /_static/manifests/com.apple.MCX manifest.plist
.. pfmkey:: com.apple.EnergySaver.portable.ACPower /_static/manifests/com.apple.MCX manifest.plist
.. pfmkey:: com.apple.EnergySaver.portable.BatteryPower /_static/manifests/com.apple.MCX manifest.plist

Power Settings Dict
^^^^^^^^^^^^^^^^^^^

.. pfm:: /_static/manifests/com.apple.MCX manifest.plist
    :key: com.apple.EnergySaver.portable.BatteryPower




Schedule
^^^^^^^^

.. pfmkey:: com.apple.EnergySaver.desktop.Schedule /_static/manifests/com.apple.MCX manifest.plist

.. pfm:: /_static/manifests/com.apple.MCX manifest.plist
    :key: com.apple.EnergySaver.desktop.Schedule

.. pfm:: /_static/manifests/com.apple.MCX manifest.plist
    :key: com.apple.EnergySaver.desktop.Schedule:RepeatingPowerOn

.. pfm:: /_static/manifests/com.apple.MCX manifest.plist
    :key: com.apple.EnergySaver.desktop.Schedule:RepeatingPowerOff

