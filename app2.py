import opendatasets as od
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
od.download('https://www.kaggle.com/abcsds/pokemon')


st.title("Pokedex Analysis")
df = pd.read_csv('pokemon/Pokemon.csv')
#print(df.head())




st.subheader("Scatter plot that shows the attack and defense capabilities of different pokemon")
fig = plt.figure(figsize=(12,6))
plt.scatter(df.Attack, df.Defense)
plt.xlabel("Attack Potency")
plt.ylabel("Defensive Potency")
st.pyplot(fig)
#plt.show()

st.subheader("Legendary Pokemon stats (mean)")
pokemon_stats_legendary = df.groupby(['Legendary', 'Generation']).mean()[['Attack', 'Defense']]
st.write(pokemon_stats_legendary)
#print(pokemon_stats_legendary)

st.subheader("Legendary Pokemon stats (median)")
pokemon_stats = df.groupby(['Legendary', 'Generation']).median()[['Attack', 'Defense']]
st.write(pokemon_stats)

st.header("Line plot showing Different attributes by generation")
fig0 = plt.figure(figsize=(12,7))
st.subheader("Blue = HP, Orange = Attack, Green = Defence,Red = Special Attack,Purple = Special Defence,Brown = Speed")
pokemon_generation = df.groupby('Generation').mean()[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
plt.plot(pokemon_generation)
st.pyplot(fig0)
#plt.show()

st.subheader("Boxplot showing variation in legendary pokemon by generation")
fig1 = plt.figure(figsize=(12,7))
sns.boxplot(x="Generation", y="Total", hue='Legendary', data=df)
st.pyplot(fig1)

st.subheader("Heatmap for different characteristics of pokemon")
fig2 = plt.figure(figsize=(12,8))
sns.heatmap(
    df.loc[:, ['HP', 'Attack', 'Sp. Atk', 'Defense', 'Sp. Def', 'Speed']].corr(),
    annot=True
)
st.pyplot(fig2)
#plt.show()