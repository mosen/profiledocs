.. _payloadtype-anything:

Custom Settings
===============

A preference may be managed by using the bundle id name as the value of the **PayloadType** variable.

You may append ``.ByHost`` to manage the preference as a ByHost preference. The MCX post composite step will automatically
apply the managed preference as a ByHost preference if this string is present.

-[MCX_PostComposite postCompositeByHost:userHome:]:


Forced
""""""

Forced is an array containing a dictionary in the following format:

.. pfm:: /_static/manifests/com.apple.ManagedClient.preferences manifest.plist
   :key: PayloadContent:PreferenceDomainHere:Forced:ForcedItem


