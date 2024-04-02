import csv
import pandas
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

TEST_SIZE = 0.4

def main_program():

    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    data, labels = load_data(sys.argv[1])
    train_data, test_data, train_labels, test_labels = train_test_split(
        data, labels, test_size=TEST_SIZE
    )

    model = train_classifier(train_data, train_labels)
    predictions = model.predict(test_data)
    sensitivity, specificity = evaluate_model(test_labels, predictions)

    print(f"Correct Predictions: {(test_labels == predictions).sum()}")
    print(f"Incorrect Predictions: {(test_labels != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(file_name):

    data = []
    labels = []

    months_dict = {'Jan': 0,
                   'Feb': 1,
                   'Mar': 2,
                   'Apr': 3,
                   'May': 4,
                   'June': 5,
                   'Jul': 6,
                   'Aug': 7,
                   'Sep': 8,
                   'Oct': 9,
                   'Nov': 10,
                   'Dec': 11}

    csv_data = pandas.read_csv(file_name)

    labels_df = csv_data['Revenue']
    data_df = csv_data.drop(columns=['Revenue'])

    data_df = data_df.replace(months_dict).infer_objects(copy=False)

    data_df['VisitorType'] = data_df['VisitorType'].apply(lambda x: 1 if x == 'Returning_Visitor' else 0)
    data_df['Weekend'] = data_df['Weekend'].apply(lambda x: 1 if x == 'True' else 0)
    labels_df = labels_df.apply(lambda x: 1 if x is True else 0)

    data_list = data_df.values.tolist()
    labels_list = labels_df.values.tolist()

    return data_list, labels_list


def train_classifier(data, labels):

    classifier = KNeighborsClassifier(n_neighbors=1)
    classifier.fit(data, labels)
    return classifier


def evaluate_model(labels, predictions):

    tn, fp, fn, tp = confusion_matrix(labels, predictions).ravel()
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)

    return sensitivity, specificity


if __name__ == "__main__":
    main_program()
