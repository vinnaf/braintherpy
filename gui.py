import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

columns = ['ms','uV']
data = pd.read_csv("Example Reteval.csv", sep=',', usecols=[2,3], skiprows=28, names=columns )
data = data.dropna(how='any')
#print(data)

pd.DataFrame.plot(data)


df1 = data[data["ms"].str.contains("ms")==False] #dropping the ms string that appears in the dataframe
col1=(df1['ms'])
col1 = np.array(col1) #converitng to np array

#for i in range(len(col1)):
#    col1[i] = int(float(col1[i]))  #converting the nteger values to floats

df1 = data[data['uV'].str.contains('mm') == False] #dropping the mm string that appears in the dataframe
col2=(df1['uV'])
col2 = np.array(col2) #converitng to np array
#for i in range(len(col2)):
#    col2[i] = int(float(col2[i]))


print(col1)
print(len(col1))
print(col2)
print(len(col2))
plt.plot(col1,col2)
plt.show()
