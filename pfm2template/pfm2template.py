#!/usr/bin/env python
# TODO: the recursion is horribad, please fix

import plistlib
import uuid
import os.path
from optparse import OptionParser

def generate_dict(data, result):
    if 'pfm_version' in data:  # Probably a top level dict
        result['PayloadType'] = 'Configuration'
        result['PayloadOrganization'] = 'Example Organization'
        result['PayloadUUID'] = str(uuid.uuid4())
        result['PayloadIdentifier'] = '{}.example'.format(data.get('pfm_domain', 'domain.undefined'))
        result['PayloadDisplayName'] = 'Example: {}'.format(data.get('pfm_title'), 'No Title')
        result['PayloadDescription'] = 'Example: {}'.format(data.get('pfm_description'), 'No Description')
        result['PayloadContent'] = [{}]

        generate(data['pfm_subkeys'], result['PayloadContent'][0])

def pfm_value(key_type, default=None, range_list=None):
    """Generate an appropriate empty value"""
    if range_list is not None:
        return range_list[0]

    if default is not None:
        return default

    if key_type == "string":
        return ""
    elif key_type == "integer":
        return 0
    elif key_type == "boolean":
        return False
    elif key_type == "dictionary":
        return {}
    elif key_type == "real":
        return 0.0
    elif key_type == "data":
        return "Base64EncodedDataHere=="
    elif key_type == "array":
        return []
    elif key_type == "date":
        return "2013-10-12T06:07:27Z"
    else:
        raise Exception("Unhandled type {}".format(key_type))

def generate_list(data, result):
    for item in data:
        if 'pfm_name' in item:  # Probably a dict key
            # print(item['pfm_name'])

            if 'pfm_subkeys' in item:  # has keys
                if item['pfm_type'] == 'array':
                    result[item['pfm_name']] = [{}]
                    generate_list(item['pfm_subkeys'], result[item['pfm_name']][0])
                else:
                    result[item['pfm_name']] = {}
                    generate_dict(item['pfm_subkeys'], result[item['pfm_name']])
            else:
                result[item['pfm_name']] = pfm_value(
                    item.get('pfm_type', 'string'),
                    item.get('pfm_default'),
                    item.get('pfm_range_list'),
                )


def generate(data, result):
    """Generate a data structure based upon the given manifest fragment"""
    if isinstance(data, dict):
        generate_dict(data, result)
    if isinstance(data, list):
        generate_list(data, result)



def generateProfile(path):
    """Generate an empty plist based upon the path given to a manifest."""
    plist = plistlib.readPlist(path)
    result = {}
    generate(plist, result)
    return result, plist['pfm_domain']


if __name__ == "__main__":
    usage = "usage: %prog [options] manifest.plist"
    parser = OptionParser(usage=usage)
    parser.add_option("-o", "--output", dest="output",
                      help="write template to output dir", metavar="DIR")

    (options, args) = parser.parse_args()

    if len(args) == 1 and options.output:
        result, domain = generateProfile(args[0])
        plistlib.writePlist(result, os.path.join(options.output, '{}.mobileconfig'.format(domain)))
    else:
        print('not enough arguments')
