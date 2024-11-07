import pandas as pd
import numpy as np

# создадим отдельную переменную dates с использованием функции date_range
# с указанием интервала времени: стартовой точки (start) в формате гггг-мм-дд,
# с указанием количества дат (10), а также интервалом (freq) в один день (D)
dates = pd.date_range(start='2022-07-26', periods=10, freq='D')


# Создадим список из случайных значений. Это можно сделать с помощью библиотеки NumPy.
# В круглых скобках укажем, сколько значений нам необходимо
values = np.random.rand(10)

# Создадим датафрейм со словарём:
df = pd.DataFrame({'Date': dates, 'Value': values})

# Установим колонку Date в качестве индекса всего датафрейма:

df.set_index('Date', inplace=True)

month = df.resample('ME').mean

print(df)
print(month)
