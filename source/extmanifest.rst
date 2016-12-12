Extended Manifest Format
========================

The manifest format covers most of the required information for writing configuration profiles, except for a few
cases.

The following is a description of keys added to the manifest format by the community as a working standard.


Suggested Keys
--------------

pfm_macos_since
^^^^^^^^^^^^^^^

Version of macOS that started supporting the key or payload.
Could also add **pfm_ios_since** and **pfm_tvos_since**.

pfm_macos_deprecated
^^^^^^^^^^^^^^^^^^^^

Version of macOS that stopped supporting the key or payload.
Can also apply to iOS and tvOS.

pfm_incompatible
^^^^^^^^^^^^^^^^

Suggest using the `pfm_target_conditions`_ dictionaries to specify rules about
how this key or payload is incompatible with the other payload or key. Usually this would
happen when one payload becomes superseded by another, and installing both results in undefined behaviour.

There's currently no way to reference other manifests so there might need to be a **pfm_target_domain** key to
match a domain in another manifest.

