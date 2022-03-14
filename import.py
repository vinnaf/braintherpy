import os
import glob
import pandas as pd

class Experiment:
    "this class serves to store an experiment with its date and results"
    pass
class Patient:
    "this class contains all the experiments of one patient"
    pass


path = r'C:\Users\veres\PycharmProjects\braintherpy\data'
csv_files = glob.glob(os.path.join(path, "*.csv"))

# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df = pd.read_csv(f, encoding = "ISO-8859-1", low_memory=False)

    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])

