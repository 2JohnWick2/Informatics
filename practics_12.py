import pandas as pd
import os 
import numpy as np

'''
Задание 1
Посчитать среднюю доходность женщин
'''
file = input("Укажите путь к нужному файлу: ")
data = file + r'\Mall_Customers.csv'
df = pd.DataFrame()

df = pd.read_csv(data, sep=",", index_col=None)
df = df.set_index(df["Genre"] == "Female")
ads = df[df['Genre'] == "Female"]["Annual Income (k$)"].mean()
print(ads)


df = pd.read_csv(data)
ads = df[df['Genre'] == 'Female']['Annual Income (k$)'].mean()
print(ads)