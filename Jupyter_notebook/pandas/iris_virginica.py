import pandas as pd
columns=['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth' , 'Species']
iris=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=columns)

df=iris.copy()

# print(df.head)

# df.columns=['SepalLength','SepalWidth', 'PetalLength', 'PetalWidth' , 'Species']

# print(df.head)

df_virginica=df[df['Species']=='Iris-virginica']
df_virginica=df_virginica[df_virginica['PetalLength']>1.5]
rows,col=(df_virginica.shape)
#a will print list of values
# a=df_virginica.values


for i in range(rows):
    output=(df_virginica.iloc[i])
    # print(type(output))
    print(output.iloc[0],output.iloc[1],output.iloc[2],output.iloc[3],output.iloc[4])
