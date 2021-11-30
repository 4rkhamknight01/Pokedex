import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#st.title("Probability Project")

df=pd.read_csv("Pokemon.csv")
print(df.head())
