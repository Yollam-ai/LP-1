# Prolog - Auto Generated #
import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

import sys
sys.tracebacklimit = 0

os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_f86a6e2e-ed3c-4f03-bd0c-012bd4ed0a02')
dataset = pandas.read_csv('input_df_8dbfd738-66dd-4109-9914-d5e1e2ec20f6.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Stage, Amount($))
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import math

indian_startup_funding =pd.read_csv("C:/Users/YollamManda/OneDrive - Lighthouse Trust/Documents/indian_startup_funding.csv")

stage = indian_startup_funding[indian_startup_funding["Stage"] != "Unknown"]

funded_stage = indian_startup_funding.groupby(stage["Stage"])["Amount($)"].sum()
funded_stage = funded_stage.sort_values(ascending=False).reset_index().head(10)
funded_stage["Amount($)"] = funded_stage["Amount($)"].apply(lambda x: math.ceil(x))
funded_stage

plt.figure(figsize=(15, 10))

# Group and sort the data
fundedstage = indian_startup_funding.groupby(stage["Stage"])["Amount($)"].sum().sort_values(ascending=False).head(10)

# Set the x and y data
x = fundedstage.index
y = fundedstage.values

plt.figure(figsize=(15, 10))

# Group and sort the data
fundedstage = indian_startup_funding.groupby(stage["Stage"])["Amount($)"].sum().sort_values(ascending=False).head(10)

# Set the x and y data
x = fundedstage.index
y = fundedstage.values

# Create a custom color map with 5 gradients of orange
custom_cmap = plt.get_cmap('Oranges')(np.linspace(0.2, 1, 5))

# Create the bar chart with the custom color map
plt.bar(x, y, color=custom_cmap)

# Set the chart title and labels
plt.title("FUNDING STAGES WITH MOST FUNDS", fontsize=20)
plt.xlabel("Funding Stage", fontsize=20)

plt.xticks(fontsize=15, rotation=80)
plt.yticks(fontsize=20)

# Show the chart
plt.show()

# Epilog - Auto Generated #
os.chdir(u'C:/Users/YollamManda/PythonEditorWrapper_f86a6e2e-ed3c-4f03-bd0c-012bd4ed0a02')
