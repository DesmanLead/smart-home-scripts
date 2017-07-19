import csv

training_set_path = '../train.csv'
testing_set_path = '../test.csv'

with open(training_set_path, 'rb') as training_file, open(testing_set_path, 'rb') as testing_file:
    training_csv = csv.reader(training_file)
    testing_csv = csv.reader(testing_file)

    X = []
    Y = []

    for row in training_csv:
        X.append(row[:-1])
        Y.append(row[-1])

    from sklearn import svm
    from sklearn.model_selection import cross_val_score

    clf = svm.SVC(decision_function_shape='ovr')

    print(cross_val_score(clf, X, Y, scoring='roc_auc'))

    clf.fit(X, Y)

    print(clf)

    X_test = []
    Y_test = []

    for row in testing_csv:
        X_test.append(row[:-1])
        Y_test.append(row[-1])

    results = clf.predict(X_test)

    right_total = 0
    wrong_total = 0

    for pair in zip(results, Y_test):
        if pair[0] == pair[1]:
            right_total += 1
        else:
            wrong_total += 1

    print('Accuracy: ' + str(float(right_total) * 100 / float(right_total + wrong_total)))
