#!/usr/bin/python
# -*- coding: utf-8 -*-

from preprocessing.data_loading import load
from sklearn import svm
from sklearn.model_selection import cross_val_score


raw_data = load('/Users/akirienko/Dropbox/Учеба/Аспирантура/SHDataActivity/Mine/*.csv')

activity_uuids = []
sensor_uuids = []

for record in raw_data:
    if record.is_activity() and record.uuid() not in activity_uuids:
        activity_uuids.append(record.uuid())
    if record.is_sensor_data() and record.uuid() not in sensor_uuids:
        sensor_uuids.append(record.uuid())

X = []
Y = []

activity_of_interest = activity_uuids[1]

current_state = [None] * len(sensor_uuids)
current_activity = None

for record in raw_data:
    uuid = record.uuid()
    if uuid in sensor_uuids:
        current_state[sensor_uuids.index(uuid)] = record.value()
        if None not in current_state and not record.is_from_dense_data_source():
            X.append(current_state)
            Y.append(1 if current_activity == activity_of_interest else -1)
    if uuid == activity_of_interest:
        if record.value() > 0.5:
            current_activity = uuid
        else:
            current_activity = None


clf = svm.SVC()

print 'AUC: %s' % cross_val_score(clf, X, Y, scoring='roc_auc')
print 'Accuracy: %s %%' % cross_val_score(clf, X, Y, scoring='accuracy')
