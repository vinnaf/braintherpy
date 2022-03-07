import pandas as pd

columns = ['Reported Waveform, Processed waveform', 'ms','uV']
data = pd.read_csv("CB07_970322_220216105506_Small.csv", sep=',', usecols=[1,2,3], skiprows=28, names=columns )
data = data.dropna(how='all')
print(data)

pd.DataFrame.plot(data)

