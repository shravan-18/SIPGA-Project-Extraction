import pandas as pd
import json


def fillCSV(f):
    with open(f, "r") as f:
        l = f.readlines()
    for i in l:
        if i == "\n":
            l.remove(i)
    titles = [string.rstrip("\n") for string in l]

    return titles


def load_csv(csv):
    # Try reading the CSV file with different encodings
    encodings_to_try = ["utf-8", "latin-1", "cp1252"]

    for encoding in encodings_to_try:
        try:
            df = pd.read_csv(csv, encoding=encoding)
            print(f"CSV file read successfully with encoding: {encoding}\n")
            return df
        except UnicodeDecodeError:
            print(f"Failed to read CSV file with encoding: {encoding}")

    return -1


def store_data(df):
    cols = df.columns
    cols = cols[:14]
    list_of_details = []
    details = {}

    print(f"Shape of data: ({df.shape[0]}, {len(cols)})\n")

    for i in range(df.shape[0]):
        for j in range(len(cols)):
            details[cols[j]] = df[cols[j]][i]
            # print(f"{cols[j]}: {df[cols[j]][i]}")

        list_of_details.append(details)

    return list_of_details


def convert_to_json(list_of_details):
    # Write the JSON data to a file
    with open("data.json", "w") as json_file:
        json.dump(list_of_details, json_file)

    print("\nData converted to JSON successfully!")
