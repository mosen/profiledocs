.. _payloadtype-com.apple.homescreenlayout:

Home Screen Layout
==================

.. figure:: /_static/ProfileManifests/Icons/ManifestsApple/com.apple.homescreenlayout.png
    :align: right
    :figwidth: 200px

:download:`Template <../_static/examples/com.apple.homescreenlayout.mobileconfig>`

The Home Screen Layout Payload defines a layout of apps, folders, and web clips for the Home screen.
It is supported on the User Channel.

.. note:: If a home screen layout puts more than six items in the iPad dock the location of the seventh and
    succeeding items may be undefined but they will not be omitted.

.. warning:: Take note that **Pages** is an array of array of dictionaries. Each item in the array is a home screen.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.homescreenlayout manifest.plist

Keys
----

Icon Dictionary
^^^^^^^^^^^^^^^

.. pfm:: /_static/manifests/com.apple.homescreenlayout manifest.plist
    :key: Dock:DockItem


.. pfmkey:: Dock:DockItem:Type /_static/manifests/com.apple.homescreenlayout manifest.plist
