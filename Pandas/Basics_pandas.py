# import pandas as pd
#
# #series
# # s = pd.Series([10,20,30],index=['a','b','c'])
# # print(s)
# #
# # #dataframe
# data = {'name':['joHn','anna'],'age':[28,32]}
# df = pd.DataFrame(data)
# print(df)
# #how do you handle missing values in pandas
# df.isnull()
# df.dropna()
# df.fillna()
#
# #How do you read data from a csv file in pandas
# df = pd.read_csv('file.csv')
#
# #how do you select a column in pandas
# df['column_name']
#
# #How do you select multiple columns
# df[['col1','col2']]
#
# #How do you filter rows based on a condition ?
# df[df['age']>30]
#
# #how do you filter using multiple conditions
# df[(df['age']>30) & (df['salary']<100000)]
#
# #how do you access rows by position
# df.iloc[0] - first row
# df.iloc[0:5] - first 5 rows