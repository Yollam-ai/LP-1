# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Location)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
indian_startup_funding =pd.read_csv("C:\Users\YollamManda\OneDrive - Lighthouse Trust\Desktop\indian_startup_funding.csv")
top_5_cities = indian_startup_funding["Location"].value_counts().head() 
colors = ['#FFA07A', '#FF8C00', '#FF7F50', '#FF6347', '#FF4500']
plt.figure(figsize=(15, 10))
plt.pie(top_5_cities, labels=indian_startup_funding["Location"].head(), 
        colors=colors, data=indian_startup_funding["Location"].value_counts())


plt.title("TOP 5 CITIES WITH MOST START-UPS", fontsize=30)
plt.show()