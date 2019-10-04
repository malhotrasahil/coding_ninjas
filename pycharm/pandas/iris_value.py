import pandas as pd

columns=['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth' , 'Species']
iris=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=columns)

df=iris.copy()

print(df.head())