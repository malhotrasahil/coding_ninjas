import pandas as pd
columns=['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth' , 'Species']
iris=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=columns)

df=iris.copy()
# print(df.head)



for i in df['Species'].value_counts():
    print(i, end=' ')


# a=df['Species'].groupby()
# print(a)

