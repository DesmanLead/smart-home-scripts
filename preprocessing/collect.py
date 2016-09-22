#!/usr/bin/python
# -*- coding: utf-8 -*-

# Beacon(name: "KitchenBeacon0", uuid: "EBEFD083-70A2-47C8-9837-E7B5634DF524", supportsIBeacon: true),
# Beacon(name: "HallBeacon1", uuid: "EBEFD083-70A2-47C8-9837-E7B5634DF525", supportsIBeacon: true),
# Beacon(name: "ToiletBeacon2", uuid: "EBEFD083-70A2-47C8-9837-E7B5634DF526", supportsIBeacon: true),
# Beacon(name: "Beacon3", uuid: "EBEFD083-70A2-47C8-9837-E7B5634DF527", supportsIBeacon: true),
# Beacon(name: "KitchenBeacon4", uuid: "EBEFD083-70A2-47C8-9837-E7B5634DF528", supportsIBeacon: true),
# Beacon(name: "Apple TV", uuid: "3ec3d2ca-4624-4943-a2f6-69e222c57393", supportsIBeacon: false),
# Beacon(name: "MI_SCALE", uuid: "bc3c94b6-9c70-4e2c-9205-0b5d3476c7d6", supportsIBeacon: false)

# "\(time)", "d9114d7c-6168-4471-805e-95c5ed325dc5", "\(rate)", "Heart Rate Sensor"

# Device(identifier: "c2bc678c-ed73-45c6-8804-bcaf645f0891", name: "Kitchen Light", isEnabled: false),
# Device(identifier: "1b0ada96-f4e0-4edc-8441-d0ed12d9ba53", name: "Kitchen Local Light", isEnabled: false),
# Device(identifier: "0b6889f4-b87c-46c5-98c9-b8c3263cd8eb", name: "Kitchen Kettle", isEnabled: false),
# Device(identifier: "ed646245-3030-4251-8320-14e228fed987", name: "Bedroom Light", isEnabled: false),
# Device(identifier: "9660cb58-ab9f-448b-add8-ed5d76e3de66", name: "Bedroom Local Light", isEnabled: false),
# Device(identifier: "0489ee1d-8919-42ce-a130-14aa0562f48b", name: "Bedroom TV", isEnabled: false),
# Device(identifier: "66ca0cbc-6d48-4264-be78-8914412f27ed", name: "Bathroom Light", isEnabled: false),
# Device(identifier: "42c46854-3ddd-4896-b271-c051e4edacb8", name: "Toilet Light", isEnabled: false),
# Device(identifier: "12421fda-3bfd-4eda-8534-ca7f5ba8bf8f", name: "Hall Light", isEnabled: false),
# Device(identifier: "dcdb6cef-f9b3-461e-81b2-54ad37736ef4", name: "Kitchen Water", isEnabled: false),
# Device(identifier: "1d145529-a34b-4b9c-94dc-df1021589cd9", name: "Bathroom Water", isEnabled: false),
# Device(identifier: "a9a2eefe-f409-45b2-92ee-d5e5cd3d29c2", name: "Bathroom Shower", isEnabled: false)

import csv

sensors = [
    'EBEFD083-70A2-47C8-9837-E7B5634DF524',  # KitchenBeacon 0
    'EBEFD083-70A2-47C8-9837-E7B5634DF528',  # KitchenBeacon 4
    'EBEFD083-70A2-47C8-9837-E7B5634DF526',  # ToiletBeacon 2
    'EBEFD083-70A2-47C8-9837-E7B5634DF527',  # BathroomBeacon 3
    'bc3c94b6-9c70-4e2c-9205-0b5d3476c7d6',  # MI_SCALE
    '3ec3d2ca-4624-4943-a2f6-69e222c57393',  # Apple TV
    'EBEFD083-70A2-47C8-9837-E7B5634DF525',  # BedroomBeacon 1
    'd9114d7c-6168-4471-805e-95c5ed325dc5',  # Heart rate sensor
]

devices = [
    'c2bc678c-ed73-45c6-8804-bcaf645f0891',
    '1b0ada96-f4e0-4edc-8441-d0ed12d9ba53',
    '0b6889f4-b87c-46c5-98c9-b8c3263cd8eb',
    'ed646245-3030-4251-8320-14e228fed987',
    '9660cb58-ab9f-448b-add8-ed5d76e3de66',
    '0489ee1d-8919-42ce-a130-14aa0562f48b',
    '66ca0cbc-6d48-4264-be78-8914412f27ed',
    '42c46854-3ddd-4896-b271-c051e4edacb8',
    '12421fda-3bfd-4eda-8534-ca7f5ba8bf8f',
    'dcdb6cef-f9b3-461e-81b2-54ad37736ef4',
    '1d145529-a34b-4b9c-94dc-df1021589cd9',
    'a9a2eefe-f409-45b2-92ee-d5e5cd3d29c2'
]

file_path = 'sample.csv'


def print_state(m_state, m_devices):
    if None in m_state:
        return
    print('(' + ', '.join(str(x) for x in m_state) + ') -> (' + ', '.join(str(x) for x in m_devices) + ')')

with open(file_path, 'rb') as db_file:

    current_state = [None, None, None, None, None, None, None, None]
    current_devices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    samples_csv = csv.reader(db_file)

    for row in sorted(samples_csv, key=lambda csv_row: csv_row[0]):
        # print(', '.join(row))
        time = row[0]
        uuid = row[1]
        state = row[2]

        if uuid in sensors:
            index = sensors.index(uuid)
            current_state[index] = state
            # Apple TV broadcasts too often
            if uuid == '3ec3d2ca-4624-4943-a2f6-69e222c57393':
                continue

            print_state(current_state, current_devices)
            continue

        if uuid in devices:
            index = devices.index(uuid)
            current_devices[index] = state
            print_state(current_state, current_devices)
            continue
