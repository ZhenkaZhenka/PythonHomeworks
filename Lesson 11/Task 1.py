# Задача 1: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

df = pd.read_csv('Lesson 11\california_housing_test.csv')

print(df[df['population'] <= 500]['median_house_value'].mean())