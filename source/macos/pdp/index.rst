Profile Domain Plugins
======================

This is basically a list of **.profileDomainPlugin** plugins, which I'm currently using to document the responsiblity
of each PayloadType.

Profile domain plugins live in ``/System/Library/CoreServices/ManagedClient.app/Contents/PlugIns``. More recently
as of Sierra some have been added to ``/System/Library/ConfigurationProfiles/PlugIns``.

In High Sierra, XPC Services are used instead, which are located within the ``ConfigurationProfiles.framework`` at
``/System/Library/PrivateFrameworks/ConfigurationProfiles.framework/XPCServices``.


.. toctree::
    :maxdepth: 2
    :caption: Profile Domain Plugins:

    adcertificate.rst
    airplay.rst
    assetcacheclient.rst
    carddav.rst
    certificate.rst
    directorybinding.rst
    dock.rst
    exchange.rst
    filevault2.rst
    firewall.rst
    font.rst
    ical.rst
    ichat.rst
    ldap.rst
    logging.rst
    loginwindow.rst
    mail.rst
    mcx.rst
    mdm.rst
    passcodepolicy.rst
    restrictionsplugin.rst
    systempolicy.rst
    touchid.rst
    vpn.rst
    webclip.rst
    wifi.rst
    xsanplugin.rst

