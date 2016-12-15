.. pwpolicy:

Password Policy
===============

:manpage:`pwpolicy(8)`

The password policy may be modified by using the :command:`pwpolicy` command line tool, or by installing a profile containing
the :ref:`payloadtype-com.apple.mobiledevice.passwordpolicy` payload.

Password policies seem to be stored as directory records.
Attempting to access password policies on an Active Directory node results in::

    Error: Operation is not supported by the directory node.



macOS 10.9
----------

Executing ``/usr/bin/pwpolicy -getglobalpolicy`` will show some of the values applied by the payload.

macOS 10.10+
------------

Executing ``/usr/bin/pwpolicy -n /Local/Default -getaccountpolicies`` will show password policies for the local directory.

Policies that have been created by profiles have a special value for **policyIdentifier**.

The identifier is generated from the **PayloadUUID** that created the policy, for example:

- The PayloadUUID might be ``777A5E39-C99E-42D9-895E-0F818F0E644B``.
- The Payload sets **maxPINAgeInDays**.
- The resulting identifier is ``ProfilePayload:777A5E39-C99E-42D9-895E-0F818F0E644B:maxPINAgeInDays``.



