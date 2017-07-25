#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import glob
from common.record import Record


def load(path):
    result = []

    for filename in glob.glob(path):
        with open(filename, 'rb') as db_file:

            samples_csv = csv.reader(db_file)

            for row in sorted(samples_csv, key=lambda csv_row: csv_row[0]):
                record = Record.parse(row)
                result.append(record)

    return result
