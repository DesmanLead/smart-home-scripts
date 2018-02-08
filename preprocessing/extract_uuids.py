#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import json
import glob
import os
from common.record import Record


uuids = {}


def verify(record):
    if record.is_activity():
        if record.is_device_state():
            print record.uuid() + ' is in Activities and Devices lists at the same time'
        if record.is_sensor_data():
            print record.uuid() + ' is in Activities and Sensors lists at the same time'

    if record.is_device_state() and record.is_sensor_data():
        print record.uuid() + ' is in Devices and Sensors lists at the same time'

    if not record.is_sensor_data() and not record.is_device_state() and not record.is_activity():
        print record.uuid() + ' is not found in any list'


def extract_uuids(file_path):
    with open(file_path, 'rb') as db_file:

        samples_csv = csv.reader(db_file)

        for row in sorted(samples_csv, key=lambda csv_row: csv_row[0]):

            record = Record.parse(row)

            verify(record)

            if not uuids.has_key(record.uuid()):
                uuids[record.uuid()] = record.description()


path = os.path.expanduser('~/Dropbox/Учеба/Аспирантура/SHDataActivity/Max/*.csv')
for filename in glob.glob(path):
    extract_uuids(filename)


print json.dumps(uuids, indent=4)
