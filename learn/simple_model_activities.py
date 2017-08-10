#!/usr/bin/python
# -*- coding: utf-8 -*-

from preprocessing.data_loading import load
from sklearn import svm
from sklearn.model_selection import cross_val_score
# from sklearn.metrics import roc_curve
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# import csv


raw_data = load('/Users/akirienko/Dropbox/Учеба/Аспирантура/SHDataActivity/Mine/*.csv')

activities = {}
activity_uuids = []
sensor_uuids = []

for record in raw_data:
    if record.is_activity() and record.uuid() not in activity_uuids:
        activity_uuids.append(record.uuid())
        activities[record.uuid()] = record
    if record.is_sensor_data() and record.uuid() not in sensor_uuids:
        sensor_uuids.append(record.uuid())

X = []
Y = []

activity_of_interest = activity_uuids[5]

current_state = [0] * len(sensor_uuids)
current_state[0] = None
current_activity = None

for record in raw_data:
    uuid = record.uuid()
    if uuid in sensor_uuids:
        current_state[sensor_uuids.index(uuid)] = record.value()
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

# with open('/Users/akirienko/Desktop/out.csv', 'wb') as out_file:
#     out_csv = csv.writer(out_file)
#
#     for row in zip(X, Y):
#         csv_row = row[0] + [row[1]]
#         out_csv.writerow(csv_row)

# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.1,
#                                                     random_state=0)
#
clf = svm.SVC()
# clf.fit(X_train, y_train)
# y_score = clf.decision_function(X_test)
#
# fpr, tpr, _ = roc_curve(y_test, y_score)
#
# plt.figure()
# lw = 2
# plt.plot(fpr, tpr, color='darkorange',
#          lw=lw, label='ROC curve')
# plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic')
# plt.legend(loc="lower right")
# plt.show()

print 'AUC: %s' % cross_val_score(clf, X, Y, scoring='roc_auc')
print 'Accuracy: %s %%' % cross_val_score(clf, X, Y, scoring='accuracy')
