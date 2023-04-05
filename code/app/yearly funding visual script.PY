# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_e86ea0ba-c5bb-45b2-84f7-becf7896f313')
dataset = pandas.read_csv('input_df_f64dfeb3-89ce-49a6-b4ef-07daa0a52a2f.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(funding_year, Amount($))
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math

indian_startup_funding =pd.read_csv("C:/Users/YollamManda/OneDrive - Lighthouse Trust/Documents/indian_startup_funding.csv")

funding_trend = indian_startup_funding.groupby("funding_year")["Amount($)"].sum()
funding_trend = funding_trend.reset_index()
funding_trend["Amount($)"] = funding_trend["Amount($)"].apply(lambda x: math.ceil(x))
funding_trend

trend = indian_startup_funding.groupby("funding_year")["Amount($)"].sum()

plt.plot(trend.index, trend.values, marker="o", color="orange")

plt.figure(figsize=(15, 7))

plt.plot(trend.index, trend.values, marker="o", color="orange")
plt.title("YEARLY FUNDING TREND", fontsize=25)

plt.xticks(trend.index, fontsize=15, rotation=45)
plt.yticks(fontsize=15)
plt.show()

# Epilog - Auto Generated #
os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_e86ea0ba-c5bb-45b2-84f7-becf7896f313')
