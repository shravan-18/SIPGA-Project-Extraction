from functions import *
import pandas as pd


def main():
    df = load_csv("SIPGA_Project_List.csv")
    for index, row in df.iterrows():
        value_a = row["Project Title"]
        value_b = row["Project Description"]
        print(f"Project Title: {value_a}, \nProject Description: {value_b}")
        break


if __name__ == "__main__":
    main()
