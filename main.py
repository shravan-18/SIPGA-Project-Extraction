from functions import *


df = load_csv("mine.csv")
details = store_data(df)

for k, v in details[0].items():
    print(f"{k}: {v}")
