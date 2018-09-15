.. _payloadtype-com.apple.mcxprinting:

Printing
========

The printing payload manages printers that should be added to the user's computer, as well as restrictions on how the
user may print.

.. note:: If the model or PPD does not exist at the time the profile is installed, it will use a Generic PostScript driver.

.. contents::

Summary
-------

.. pfmheader:: /_static/manifests/com.apple.mcxprinting manifest.plist

Keys
----

.. pfmkey:: DefaultPrinter /_static/manifests/com.apple.mcxprinting manifest.plist
.. pfm:: /_static/manifests/com.apple.mcxprinting manifest.plist
    :key: DefaultPrinter


.. pfmkey:: UserPrinterList /_static/manifests/com.apple.mcxprinting manifest.plist

.. pfm:: /_static/manifests/com.apple.mcxprinting manifest.plist
    :key: UserPrinterList

.. pfm:: /_static/manifests/com.apple.mcxprinting manifest.plist
    :key: UserPrinterList:QueueName

.. pfmkey:: RequireAdminToAddPrinters /_static/manifests/com.apple.mcxprinting manifest.plist
.. pfmkey:: AllowLocalPrinters /_static/manifests/com.apple.mcxprinting manifest.plist
.. pfmkey:: RequireAdminToPrintLocally /_static/manifests/com.apple.mcxprinting manifest.plist
.. pfmkey:: ShowOnlyManagedPrinters /_static/manifests/com.apple.mcxprinting manifest.plist
.. pfmkey:: PrintFooter /_static/manifests/com.apple.mcxprinting manifest.plist
.. pfmkey:: PrintMACAddress /_static/manifests/com.apple.mcxprinting manifest.plist
.. pfmkey:: FooterFontSize /_static/manifests/com.apple.mcxprinting manifest.plist
.. pfmkey:: FooterFontName /_static/manifests/com.apple.mcxprinting manifest.plist


Links
-----

- Setting print queue options (OUTDATED) `OS X Mavericks: Setting print queue authentication method via profile <https://support.apple.com/en-qa/HT200262>`_.
