import sys
import json
import operator

"""
Catalog REST endpoint:
https://kauppa.saunalahti.fi/rest/products/catalog

ALL CATALOG ITEM KEYS:
mobilePhone: [],
otherDevice: [],
mobileSubscription: [],
mobileBroadband: [],
securityProduct: [],
crossSellableDevices: [],
contractualPrepaid: [],
pilvilinnaProduct: [],
office365Product: [],
fixedMobile: [],
tablet: [],
laptop: [],
viihdeProduct: []
"""

def print_all(catalog):
    for key in catalog:
        print '-------- ' + key + ' --------'
        devices = catalog[key]
        for device in devices:
            print device.get('uid', '') + str(device.get('productId', '')) + ' ' + device.get('description', '') + ' ' \
            + device.get('vendor', '') + ' ' + device.get('model', '')

# All ids and names
def print_ids1(catalog, key):
    print '-------- ' + key + ' --------'
    devices = catalog[key]
    for device in devices:
        print str(device['deviceTypeId']) + ', -- ' + device['uid'] + ' ' + device['vendor'] + ' ' + device['model']
    return len(devices)

# Unique device ids and names (optionally deviceType)
def print_ids(catalog, key):
    print '-------- ' + key + ' --------'
    devices = catalog[key]
    s = ''
    dev_ids = dict()
    for device in devices:
        name = device['vendor'] + ' ' + device['model']
        if key == 'otherDevice':
            name += ' (' + device.get('deviceType') + ')'
        dev_ids[device['deviceTypeId']] = name
    sorted_names = sorted(dev_ids.items(), key=operator.itemgetter(1))
    for id, name in sorted_names:
        print str(id) + ': ' + name
    return len(dev_ids)

# Unique device ids only
def print_ids3(catalog, key):
    print '-------- ' + key + ' --------'
    devices = catalog[key]
    s = ''
    dev_ids = set()
    for device in devices:
        dev_ids.add(device['deviceTypeId'])
    for id in sorted(dev_ids):
        s += str(id) + ','
    print s
    return len(dev_ids)

def print_device(devices, id):
    for device in devices:
        if device['deviceTypeId'] == id:
            print json.dumps(device, indent=4, sort_keys=False)

def main():
    file = open('catalog.json', 'r')
    data = json.loads(file.read())
    count = 0
    count += print_ids(data, 'mobilePhone')
    count += print_ids(data, 'otherDevice')
    count += print_ids(data, 'tablet')
    count += print_ids(data, 'laptop')
    print 'Count: ' + str(count)
    #print_device(data['laptop'], 1866)
    #print_all(data)


if __name__ == '__main__':
    main()
