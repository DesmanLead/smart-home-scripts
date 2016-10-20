import csv

data_set_path = '../output.csv'
training_set_path = '../train.csv'
testing_set_path = '../test.csv'

with open(data_set_path, 'rb') as ds_file, \
        open(training_set_path, 'wb') as training_set_file, \
        open(testing_set_path, 'wb') as testing_set_file:

    samples_csv = csv.reader(ds_file)
    training_set_csv = csv.writer(training_set_file)
    testing_set_csv = csv.writer(testing_set_file)

    total_samples = sum(1 for row in samples_csv)

    training_set_size = total_samples * 3 / 4

    ds_file.seek(0)

    for idx, row in enumerate(samples_csv):
        if idx < training_set_size:
            training_set_csv.writerow(row)
        else:
            testing_set_csv.writerow(row)
