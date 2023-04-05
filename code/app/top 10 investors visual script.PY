# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_6b3ad91b-5fb2-4f05-98d9-6c184120c5da')
dataset = pandas.read_csv('input_df_cd271c4a-7fc4-4085-8d7a-9f0b47d2969b.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Investor)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
indian_startup_funding =pd.read_csv("C:/Users/YollamManda/OneDrive - Lighthouse Trust/Documents/indian_startup_funding.csv")
investors = indian_startup_funding[indian_startup_funding["Investor"]!="Unknown"]

top_10_investors = pd.DataFrame(investors["Investor"].value_counts().head(10))
top_10_investors
top_10_investors = investors["Investor"].value_counts().head(10)

colors = ['#FFA07A', '#FF8C00', '#FF7F50', '#FF6347', '#FF4500']

# create the plot
plt.figure(figsize=(15, 10))
plt.barh(top_10_investors.index, top_10_investors.values, color=colors)
plt.title("TOP 10 INVESTORS BY NUMBER OF FUNDS", fontsize=25)

plt.ylabel("Investors", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.gca().invert_yaxis()
plt.show()


# Epilog - Auto Generated #
os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_6b3ad91b-5fb2-4f05-98d9-6c184120c5da')
