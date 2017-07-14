PostComposite - Kerberos
========================

This post composite step seems to exist to substitute the user shortname into the kerberos login domain.

Sequence
--------

- Get effective UID
- Get preferences in domain ``edu.mit.Kerberos.KerberosLogin``.
- MCX PostComposite username w **KLName**
- Write preferences ``edu.mit.Kerberos.KerberosLogin``.
- Log "MCX -postCompositeKerberos, [mutableKerberosUserPrefs writePrefsInDomain:%s withHomePath:%s]== %d"
