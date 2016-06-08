#!/usr/bin/python3.4
# coding: utf-8

import sys
import platform

def getConntrack(conntrackVar):
    """
    This function gets the value of the conntrack variable passed in argument.
    """
    conntrackVar = "{}/{}".format(conntrackPath,conntrackVar)
    try:
        with open('{}'.format(conntrackVar), 'r') as f:
            conntrackValue = int(f.read().replace('\n',''))
    except IOError as e:
        print('UNKNOWN | \"{}\" does not exist! '
              'Please check the conntrackPath.'.format(conntrackPath))
        sys.exit(3)
    return conntrackValue

try:
    linuxFamily = str.lower(platform.linux_distribution()[0])
except:
    print('UNKNOWN | Error detecting linuxFamily')
    sys.exit(3)

# if you want to enforce the linuxFamily uncomment the line you need
#linuxFamily = 'debian'    # Enforce debian linuxFamily
#linuxFamily = 'redhat'    # Enforce redhat linuxFamily

if linuxFamily == 'debian' or linuxFamily == 'ubuntu':
    conntrackPath = '/proc/sys/net/netfilter'
elif linuxFamily == 'redhat' or linuxFamily == 'centos':
    conntrackPath = '/proc/sys/net/'

try:
    conntrackMax = getConntrack('nf_conntrack_max')
    conntrackCount = getConntrack('nf_conntrack_count')
    if conntrackMax > 0 and conntrackCount > 0:
        try:
            conntrackPrct = ( conntrackCount / conntrackMax ) * 100
            if conntrackPrct >= 90:
                print('CRITICAL | {:.1f}% conntrack used'.format(conntrackPrct))
                sys.exit(2)
            elif conntrackPrct >= 75:
                print('WARNING | {:.1f}% conntrack used'.format(conntrackPrct))
                sys.exit(1)
            elif conntrackPrct < 75:
                print('OK | {:.1f}% conntrack used'.format(conntrackPrct))
                sys.exit(0)
        except NameError as e:
            print('UNKNOWN | ' + e)
            sys.exit(3)
    elif conntrackMax < 0:
        raise ValueError('UNKNOWN | conntrackMax is null or negative')
        sys.exit(3)
    elif conntrackCount < 0:
        raise ValueError('UNKNOWN | conntrackCount is null or negative')
except Exception as e:
    print('UNKNOWN | Unknown error: ' + e)
