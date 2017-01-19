.. _payloadtype-com.apple.familycontrols.timelimits:

Parental Controls - Time Limits
===============================

This payload controls time allowances and curfews as shown in the Parental Controls system preference pane.

Summary
-------

.. pfmheader:: manifests/manual/com.apple.familycontrols.timelimits manifest.plist
.. pfm:: manifests/manual/com.apple.familycontrols.timelimits manifest.plist

Keys
----

.. pfmkey:: familyControlsEnabled manifests/manual/com.apple.familycontrols.timelimits manifest.plist
.. pfmkey:: limits-list manifests/manual/com.apple.familycontrols.timelimits manifest.plist

Time Limits Item
^^^^^^^^^^^^^^^^

.. pfm:: manifests/manual/com.apple.familycontrols.timelimits manifest.plist
    :key: limits-list:limits-list-item


Allowances Item
^^^^^^^^^^^^^^^

.. pfm:: manifests/manual/com.apple.familycontrols.timelimits manifest.plist
    :key: limits-list:limits-list-item:allowances:allowances-item


Curfews
^^^^^^^

.. pfm:: manifests/manual/com.apple.familycontrols.timelimits manifest.plist
    :key: limits-list:limits-list-item:curfews

