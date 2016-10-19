import csv

data_set_path = '../output.csv'

with open(data_set_path, 'rb') as ds_file:
    samples_csv = csv.reader(ds_file)

    X = []
    Y = []

    for row in samples_csv:
        X.append(row[:-1])
        Y.append(row[-1])

    from sklearn import svm

    clf = svm.SVC(decision_function_shape='ovr')
    clf.fit(X, Y)
    print(clf.predict([[0, 0, -82, -77, -61, -59, 0, 86.0]]))
    print(clf.predict([[0, 0, -82, -77, -61, -61, 0, 86.0]]))
