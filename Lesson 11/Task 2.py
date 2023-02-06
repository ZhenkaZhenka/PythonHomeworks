# Задача 2: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd

df = pd.read_csv('Lesson 11\california_housing_test.csv')

print(df[df['population'] == df['population'].min()]['households'].max())