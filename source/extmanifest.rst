Extended Manifest Format
========================

The manifest format covers most of the required information for writing configuration profiles, except for a few
cases.

The following is a description of keys added to the manifest format by the community as a working standard.


Extended Keys
-------------

pfm_macos_min
^^^^^^^^^^^^^

Version of macOS that started supporting the key or payload.

pfm_macos_max
^^^^^^^^^^^^^

Version of macOS that stopped supporting the key or payload.

pfm_ios_min
^^^^^^^^^^^

Version of iOS that started supporting the key or payload.

pfm_ios_max
^^^^^^^^^^^

Version of iOS that stopped supporting the key or payload.

pfm_tvos_min
^^^^^^^^^^^^

Version of tvOS that started supporting the key or payload.

pfm_tvos_max
^^^^^^^^^^^^

Version of tvOS that stopped supporting the key or payload.

pfm_supervised
^^^^^^^^^^^^^^

Bool true/false, requires device to be supervised for this setting to work.
Additionally, we will interpret this to mean that UAMDM is required for macOS.

pfm_incompatible
^^^^^^^^^^^^^^^^

Suggest using the **pfm_target_conditions** dictionaries to specify rules about
how this key or payload is incompatible with the other payload or key. Usually this would
happen when one payload becomes superseded by another, and installing both results in undefined behaviour.

There's currently no way to reference other manifests so there might need to be a **pfm_target_domain** key to
match a domain in another manifest.
