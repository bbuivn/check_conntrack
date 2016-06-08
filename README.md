check_conntrack.py
==================

This is a Nagios / Shinken script to get the conntrack usage in percent.

It works for two linux families:
* Debian
  * Debian
  * Ubuntu
* RedHat
  * RedHat
  * Centos

Manualy force the Linux family
------------------------------
You can enforce the Linux Family of you (only Debian or RedHat) by uncommenting one of these lines:
```
#linuxFamily = 'debian'    # Enforce debian linuxFamily
#linuxFamily = 'redhat'    # Enforce redhat linuxFamily
```
