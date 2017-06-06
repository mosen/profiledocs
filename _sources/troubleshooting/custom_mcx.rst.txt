Custom MCX Sequence
===================

Custom MCX Settings are applied via ManagedClient itself, not a payload domain plugin.

``- [MCXD_MCX loadConfigDataFromCoreData:withCompositorDict:withUserState:]``

-> 

``- [MCX_ConfigPayload createMCXSettingsArrays]``

- call ``payloadApplicationDomain`` to retrieve the domain this setting applies to.
    - This checks that there is only a single MCX domain. If more than 1, we bail.
    - TODO: follow up on domain translation

- check the payload content for legacy settings, if it is legacy then this message should be logged::

    MCX_ConfigPayload.hasLegacySettings = %d

- If the payload key points to an array, then it is not considered to be legacy settings, otherwise if it is a dict,
    continue on.

- Check the ``mcx_preference_settings`` key in each item.

- If this contains ``ByHost`` or ``Set-Once``, then there are some separate keys to consider.
- ``mcx_application_data``.
- ``mcx_precedence``.
- Tries to create the property list. I assume in managed preferences

