import pandas as pd

df = pd.read_excel("D:/employees.xlsx")

# print(df)

# df.isnull().sum()

# df.drop_duplicates(inplace=True)

df.info()

df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])

df.to_csv("clean_hr.csv", index=False)


