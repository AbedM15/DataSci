import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from scipy.stats import iqr
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


df = pd.read_csv("data/Mall_Customers.csv", sep="\t")
df.head()

sns.histplot(data=df, x=df["Age"] ,kde=True,bins=list(range(10,150,10)))
plt.title("Age distribution")