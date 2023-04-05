# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_046c6946-6ce6-49eb-b3b4-41210e8c0cd0')
dataset = pandas.read_csv('input_df_816a1d3d-1d5c-454c-8440-3eeaecc7c7b9.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Location, Amount($))
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import seaborn as sns
indian_startup_funding =pd.read_csv("C:/Users/YollamManda/OneDrive - Lighthouse Trust/Documents/indian_startup_funding.csv")

city = indian_startup_funding[indian_startup_funding["Location"] != "Unknown"]

city_funding = indian_startup_funding.groupby(city["Location"])["Amount($)"].sum()
city_funding = city_funding.sort_values(ascending=False).reset_index()
city_funding["Amount($)"] = city_funding["Amount($)"].apply(lambda x: math.ceil(x))


city_Funding = city_funding[city_funding["Location"] != "California"]
city_Funding.head(10)

orange_colors = sns.color_palette("Oranges_r", 5)

# Create the bar plot
plt.figure(figsize=(15, 10))
sns.barplot(x="Location", y="Amount($)", data=city_Funding.head(10), palette=orange_colors)
plt.title("CITIES WITH HIGHEST FUNDS", fontsize=20)


plt.xticks(fontsize=15, rotation=80)
plt.yticks(fontsize=15)
plt.show()



# Epilog - Auto Generated #
os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_046c6946-6ce6-49eb-b3b4-41210e8c0cd0')
