.. _payloadtype-com.apple.familycontrols.timelimits.v2:

Parental Controls - Time Limits
===============================
:download:`Template <../_static/examples/com.apple.familycontrols.timelimits.v2.mobileconfig>`

This payload controls time allowances and curfews as shown in the Parental Controls system preference pane.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.familycontrols.timelimits.v2 manifest.plist

Keys
----

.. pfmkey:: familyControlsEnabled /_static/manifests/com.apple.familycontrols.timelimits.v2 manifest.plist


limits-list
^^^^^^^^^^^

Allowances and Curfews by weekday or weekend.

.. pfm:: /_static/manifests/com.apple.familycontrols.timelimits.v2 manifest.plist
    :key: limits-list


Each of these keys contains a dictionary in the following format:

.. pfm:: /_static/manifests/com.apple.familycontrols.timelimits.v2 manifest.plist
    :key: limits-list:weekday-allowance


