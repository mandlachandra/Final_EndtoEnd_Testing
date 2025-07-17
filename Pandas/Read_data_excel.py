import pandas as pd

df = pd.read_excel("data.xlsx")

for index,row in df.iterrows():
    print(f"username: {row['username']},password: {row['password']}")