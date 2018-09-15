#!/usr/bin/env python

import plistlib
import json
import os.path
from os import listdir
from datetime import datetime
import logging
from optparse import OptionParser

logger = logging.getLogger('pfm2index')

def generate_item(manifest_path):
    print('processing: {}'.format(manifest_path))
    try:
        p = plistlib.readPlist(manifest_path)
        result = {
            'ManifestPath': manifest_path,
            'PayloadType': p['pfm_domain'],
            'PayloadDisplayName': p.get('pfm_title', None),
            'PayloadDescription': p['pfm_description'],
            'PayloadIOSMinVersion': p.get('pfm_ios_min', None),
            'PayloadIOSMaxVersion': p.get('pfm_ios_max', None),
            'PayloadMacOSMinVersion': p.get('pfm_macos_min', None),
            'PayloadMacOSMaxVersion': p.get('pfm_macos_max', None),
            'PayloadTvOSMinVersion': p.get('pfm_tvos_min', None),
            'PayloadTvOSMaxVersion': p.get('pfm_tvos_max', None),
            'PayloadSingleton': p.get('pfm_unique', False),
            'PayloadSupervisionRequired': p.get('pfm_supervised', False),
        }
    except ValueError as e:
        result = {'ManifestPath': manifest_path, 'error': True, 'errorMessage': e.message}
        print('skipping: {}'.format(manifest_path))
        pass

    return result


if __name__ == "__main__":
    usage = "usage: %prog [options] /path/to/manifests"
    parser = OptionParser(usage=usage)
    parser.add_option("-o", "--output", dest="output",
                      help="write index to output dir", metavar="DIR")

    (options, args) = parser.parse_args()

    ch = logging.StreamHandler()
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)
    result = {
        "version": "1.0",
        "lastUpdatedUtc": datetime.utcnow().isoformat(),
        "payloads": [],
    }

    result['payloads'] = [generate_item(os.path.join(args[-1], f)) for f in listdir(args[-1])]

    if options.output:
        with open(os.path.join(options.output, 'payload-index.json'), 'w+') as f:
            json.dump(result, f, indent=4)
    else:
        print(json.dumps(result))
