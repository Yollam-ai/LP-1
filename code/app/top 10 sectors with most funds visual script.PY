# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_78ec06bc-9402-42ab-92c0-6597262a7cc1')
dataset = pandas.read_csv('input_df_2d31c51f-8244-48b4-99bf-d2be57cfbe00.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Amount($), Sector)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

indian_startup_funding =pd.read_csv("C:/Users/YollamManda/OneDrive - Lighthouse Trust/Documents/indian_startup_funding.csv")

ten_top_industries = indian_startup_funding.groupby("Sector")["Amount($)"].sum().sort_values(ascending=False).head(10)
colors = ['#FFA07A', '#FF8C00', '#FF7F50', '#FF6347', '#FF4500']

# create the plot
plt.figure(figsize=(15, 10))
plt.barh(ten_top_industries.index, ten_top_industries.values, color=colors)
plt.title("TOP TEN SECTORS WITH HIGHEST FUNDING", fontsize=20)
plt.xlabel("Amount($'Billion)", fontsize=20)
plt.ylabel("Sector", fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=10)
plt.gca().invert_yaxis()
plt.show()


# Epilog - Auto Generated #
os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_78ec06bc-9402-42ab-92c0-6597262a7cc1')
