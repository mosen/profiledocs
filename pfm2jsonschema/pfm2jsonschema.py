#!/usr/bin/env python

import plistlib
import json
import os.path
import logging
from optparse import OptionParser

logger = logging.getLogger('pfm2jsonschema')

def generate_pfm_header(data, result):
    """Generate a top-level JSON schema"""
    result['title'] = data.get('pfm_domain', 'Untitled')
    result['type'] = 'object'

    properties = {}
    generate(data['pfm_subkeys'], properties)

    result['properties'] = properties

def pfm_to_jsontype(pfm_type):
    """Return the JSON Schema form of the given pfm_type"""
    translated = {
        'integer': 'number',
        'real': 'number',
        'data': 'string',
        'date': 'string',
        'dictionary': 'object'
    }

    if pfm_type in translated:
        return translated[pfm_type]
    else:
        logger.debug("possibly unhandled pfm_type: {}".format(pfm_type))
        # Types that are identically named: array, string
        return pfm_type

def generate_pfm_item(data, result):
    """Generate a JSON Schema object from a pfm item i.e an item in the schema that has at least a pfm_name."""
    logger.debug("generating schema for property: {}".format(data['pfm_name']))

    if data['pfm_name'] in result:
        raise Exception('Already in properties dict: {}'.format(data['pfm_name']))

    prop = {}
    prop['type'] = pfm_to_jsontype(data['pfm_type'])

    if 'pfm_description' in data:
        prop['description'] = data['pfm_description']

    if 'pfm_default' in data:
        # TODO: need processing of dict defaults
        prop['default'] = data['pfm_default']

    if 'pfm_range_list' in data:
        prop['enum'] = data['pfm_range_list']

    if 'pfm_range_min' in data:
        prop['minimum'] = data['pfm_range_min']

    if 'pfm_range_max' in data:
        prop['maximum'] = data['pfm_range_max']

    if 'pfm_format' in data:
        prop['pattern'] = data['pfm_format']

    if data['pfm_type'] == 'date':
        prop['format'] = 'date-time'  # Use predefined RFC3339 formatting

    if 'pfm_subkeys' in data:
        if prop['type'] == 'array':
            prop['items'] = {}
            # Have to discard the pfm_name in the items sub schema

            item = {}
            generate(data['pfm_subkeys'][0], item)
            name, value = item.items()[0]

            prop['items'] = value
        else:
            prop['properties'] = {}
            generate(data['pfm_subkeys'], prop['properties'])

    result[data['pfm_name']] = prop


def generate(data, result):
    """Generate a JSON Schema object as a dict from a parsed plist manifest given as a dict"""
    logger.debug("generate()")

    if isinstance(data, dict):
        if 'pfm_name' in data:
            logging.debug("generate pfm dict: {}".format(data['pfm_name']))
            return generate_pfm_item(data, result)
        elif 'pfm_version' in data: # probably top level dict
            logging.debug("generate pfm header")
            generate_pfm_header(data, result)
        else:
            logger.debug("generate non pfm dict")
    elif isinstance(data, list):
        logger.debug("generating list")
        for item in data:
            generate(item, result)
    else:
        logger.debug("unhandled type")

    return None


if __name__ == "__main__":
    usage = "usage: %prog [options] manifest.plist"
    parser = OptionParser(usage=usage)
    parser.add_option("-o", "--output", dest="output",
                      help="write template to output dir", metavar="DIR")

    (options, args) = parser.parse_args()

    ch = logging.StreamHandler()
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)

    plist = plistlib.readPlist(args[-1])
    domain = plist['pfm_domain']

    result = {
        "$schema": "http://json-schema.org/schema#"
    }
    generate(plist, result)

    if options.output:
        with open(os.path.join(options.output, '{}.json'.format(domain)), 'w+') as f:
            json.dump(result, f, indent=4)
    else:
        print(json.dumps(result))
