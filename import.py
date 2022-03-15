import os
import glob
import pandas as pd
import csv


class Experiment:
    "this class serves to store an experiment with its date and results"
    #date, electrode type, eye, results, etc

    #order by date (ascending)

    #function to get data easily

    pass

#class Patient: #first try with a single dictionary is enough
    #"this class contains all the personal data and all the experiments of one patient"

    #ID, birth date, etc, experiments

    #pass


# DATA READING
path = r'C:\Users\veres\PycharmProjects\braintherpy\data'
csv_files = glob.glob(os.path.join(path, "*.csv"))
d={}
for f in csv_files: # loop over the list of csv files
    df = pd.read_csv(f, encoding = "ISO-8859-1", low_memory=False, usecols=[1, 2], header=None) # read the csv file
    df=df.values
    df.tolist() #easier to use the table as a list of lists(rows)
    s=df[0][1] #I tried to get the real value (for example the patient ID)
    d[s]=df[1][1]
print(d)

