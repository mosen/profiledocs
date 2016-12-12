Manifest File Format
====================

The manifest file format originates with ManagedClient on Mac OS X 10.6 (maybe even earlier).

At a basic level, it is a plist file that describes the structure of another plist file.
It also contains information about which keys are dependent on other parts of the plist.

Some keys have been added for the newer configuration profile system as you can see from the manifests included with
Apple Configurator 2.

This document is a basic attempt to document the format. All of the payload documentation is generated from these files.



