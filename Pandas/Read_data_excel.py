import pandas as pd

df = pd.read_excel("C://Users//DELL//OneDrive//Desktop//Credentials.xlsx")

for index,row in df.iterrows():
    print(f"username: {row['username']},password: {row['password']}")