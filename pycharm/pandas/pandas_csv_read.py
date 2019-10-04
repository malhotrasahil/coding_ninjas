import pandas as pd

iris=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

print(type(iris))



df = iris.copy()


df.columns=['sl','sw','pl','pw','flower']


# print(df.head(10))
# print(df.shape)
# print(iris.shape)
#
# col=df.iloc[1:2,0:3]
# print(type(col))
#
# print(df.dtypes)
# print(df.describe())
print(df.drop(1, inplace=True))
# print(df.head)
print(df.drop(df.index[3], inplace=True))
print(df.head)

print(df.loc[7])
print(df.iloc[7])
