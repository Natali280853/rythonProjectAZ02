import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt


data = {'value': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)

# Создадим график, который поможет визуализировать данные из датафрейма
# df['value'].hist()
# plt.show()

# df.boxplot(column='value')
# plt.show()

print(df.describe())

df.boxplot(column='value')
plt.show()

# Далее определим первый (Q1) и третий (Q3) квартили, используя функцию quantile():

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)

# Теперь рассчитаем межквартальный размах (IQR), для этого пропишем
IQR = Q3 - Q1

# На основе вычисленных значений определим нижнюю и верхнюю границы для определения выбросов.
# Пропишем переменные для границ:
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

# А теперь необходимо удалить выбросы, которые не входят в очерченный диапазон.
# Создадим новый датафрейм:

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]

df_new.boxplot(column='value')
plt.show()
