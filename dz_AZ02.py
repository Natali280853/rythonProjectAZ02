import pandas as pd
import numpy as np

# таблица из 10 учеников с оценками учеников по 5 разным предметам.
# создайте DataFrame с данными
# Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# Вычислите среднюю оценку по каждому предмету
# Вычислите медианную оценку по каждому предмету
# Вычислите Q1 и Q3 для оценок по математике:
# Q1_math = df['Математика'].quantile(0.25)
# Q3_math = df['Математика'].quantile(0.75)
#
# можно также попробовать рассчитать IQR
# Вычислите стандартное отклонение

data = {
    'Ученик': [f'Ученик {i + 1}' for i in range(10)],
    'Математика': np.random.randint(2, 6, size=10),
    'Физика': np.random.randint(2, 6, size=10),
    'Химия': np.random.randint(2, 6, size=10),
    'История': np.random.randint(2, 6, size=10),
    'Литература': np.random.randint(2, 6, size=10)
}

df = pd.DataFrame(data)

# 2. Вывод первых нескольких строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head(10))

# 3. Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores.to_string(index=True))

# 4. Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores.to_string(index=True))

# 5. Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nQ1 по математике:", Q1_math)
print("Q3 по математике:", Q3_math)
print("IQR по математике:", IQR_math)

# 6. Вычисление стандартного отклонения
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation.to_string(index=True))
