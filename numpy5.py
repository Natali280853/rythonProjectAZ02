import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)

# Преобразуем столбцы в категориальные данные. Мы можем сделать категории
# для столбцов "gender" и "department":
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

# Команда astype преобразует гендер и департамент в категориальный тип, что позволяет
# работать с этими данными как с категориями.
# Чтобы просмотреть уникальные категории, которые есть в датафрейме, напишем и запустим код:
print(df['gender'].cat.categories)
print(df['department'].cat.categories)

# посмотреть числовые коды категорий:
print(df['gender'].cat.codes)

# добавить новую категорию — например, новый департамент, финансовый отдел.
# Для этого прописываем место, куда хотим добавить новые сведения (department):
df['department'] = df['department'].cat.add_categories(['Finance'])

# Чтобы увидеть изменения в датафрейме:
print(df['department'].cat.categories)

# мы можем удалить категорию. Для этого вместо команды add нужно прописать remove:
df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)
print(df)

