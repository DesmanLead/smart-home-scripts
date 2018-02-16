#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from preprocessing.data_loading import load
from preprocessing.filters import MovingAverage
from sklearn import svm
from sklearn.model_selection import cross_val_score

data_folder_path = os.path.expanduser('~/Dropbox/Учеба/Аспирантура/SHDataActivity/Mine/*.csv')
raw_data = load(data_folder_path)

activities = {}
activity_uuids = []
sensor_uuids = []

for record in raw_data:
    if record.is_activity() and record.uuid() not in activity_uuids:
        activity_uuids.append(record.uuid())
        activities[record.uuid()] = record
    if record.is_sensor_data() and record.uuid() not in sensor_uuids:
        sensor_uuids.append(record.uuid())

for activity_of_interest in activity_uuids:
    X = []
    Y = []

    current_state = [0] * len(sensor_uuids)
    current_state[0] = None
    current_activity = None

    ma_filters = [MovingAverage(0, size=8) for n in range(len(sensor_uuids))]

    for record in raw_data:
        uuid = record.uuid()

        if uuid in sensor_uuids:
            index = sensor_uuids.index(uuid)

            # filtering
            value = record.value()
            if record.is_beacon_rssi() and value == 0:
                value = -255
            ma_filters[index].put(value)

            current_state[index] = ma_filters[index].filtered_value()

            # appending feature vector if needed
            if None not in current_state and not record.is_from_dense_data_source():
                X.append(list(current_state))
                Y.append(1 if current_activity == activity_of_interest else -1)

        if uuid == activity_of_interest:
            if record.value() > 0.5:
                current_activity = uuid
            else:
                current_activity = None

    activity_name = activities[activity_of_interest].description()
    print 'Evaluation results for activity: %s' % activity_name

    clf = svm.SVC()

    print 'AUC: %s' % cross_val_score(clf, X, Y, scoring='roc_auc')
    print 'Accuracy: %s %%' % cross_val_score(clf, X, Y, scoring='accuracy')
