import argparse
import os
import plistlib

parser = argparse.ArgumentParser(description='Create a payload manifest index as a dict')
parser.add_argument('source',
                    help='Source directory',
                    metavar='dir')


if __name__ == '__main__':
    args = parser.parse_args()

    index = []
    url_prefix = 'https://mosen.github.io/profiledocs/_downloads/'

    for name in os.listdir(args.source):
        if not os.path.splitext(name)[1] == '.mobileconfig':
            continue

        print name
        mc = plistlib.readPlist(os.path.join(args.source, name))

        if 'PayloadContent' not in mc:
            print 'broken'
            continue
        first_payload = mc['PayloadContent'][0]
        index.append({
            'PayloadType': first_payload.get('PayloadType', ''),
            'PayloadDisplayName': first_payload.get('PayloadDisplayName', ''),
            'PayloadDescription': first_payload.get('PayloadDescription', ''),
            'URL': '{}{}'.format(url_prefix, name)
        })

    output = plistlib.writePlistToString(index)
    print output