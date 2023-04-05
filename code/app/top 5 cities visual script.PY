# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_df3988a6-13da-4ce2-a4e6-7fa42f46b4d0')
dataset = pandas.read_csv('input_df_c17f5eec-2080-4d93-93cd-88eea2e6a6f3.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Location)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
indian_startup_funding =pd.read_csv("C:/Users/YollamManda/OneDrive - Lighthouse Trust/Documents/indian_startup_funding.csv")
top_5_cities = indian_startup_funding["Location"].value_counts().head() 
colors = ['#FFA07A', '#FF8C00', '#FF7F50', '#FF6347', '#FF4500']
plt.figure(figsize=(15, 10))
plt.pie(top_5_cities, labels=indian_startup_funding["Location"].head(), 
        colors=colors, data=indian_startup_funding["Location"].value_counts())


plt.title("TOP 5 CITIES WITH MOST START-UPS", fontsize=30)
plt.show()


# Epilog - Auto Generated #
os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_df3988a6-13da-4ce2-a4e6-7fa42f46b4d0')
