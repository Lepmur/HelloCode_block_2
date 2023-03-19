import pandas as pd

df = pd.read_csv('california_housing_train.csv', sep=',') # sep=';' по умолчанию, можно не указывать

#========================================About_TABLE=================================================

# print(df.head(n=10)) # вывод первых n строк, по умолчанию n=5, можно не указывать

# print(df.tail(n=10)) # вывод последних n строк, по умолчанию n=5, можно не указывать

# print(df.shape) # вывод инф о таблице (кол-во строк и столбцов)

# print(df.isnull()) # вывод инф о пустых значениях

# print(df.isnull().sum()) # вывод суммы (итога) пустых значений по каждому столбцу

# print(df.dtypes) # вывод типа данных столбцов

# print(df.columns) # вывод названий столбцов

#==============================SELECT_DATA====================================

#print(df[['longitude', 'totalRooms', 'medianHouseValue']]) # вывод только нужных столбцов

# Вывести столбец total_rooms, у которого housing_median_age < 20
#print(df[df['housingMedianAge'] < 20]['totalRooms'])
# Вывести столбец total_rooms и housingMedianAge у которых 10 < housing_median_age < 20
#print(df[(df['housingMedianAge'] < 20) & (df['housingMedianAge'] > 10)][['totalRooms', 'housingMedianAge']])

#==============================STATISTIC====================================

# print(df['population'].max()) # выведет максимальное значение в столбце population
#
# print(df['population'].min()) # выведет минимальное значение в столбце population
#
# print(df['population'].mean()) # выведет среднее значение в столбце population
#
# print(df['population'].sum()) # выведет сумму столбца population
#
# print(df[['population', 'totalRooms']].median()) # выведет средние значения по указанным столбцам

# print(df.describe()) # сборная статистика по всей таблице:
                        # count - общее значение не пустых строк
                        # mean - среднее значение в каждом столбце
                        # std - стандартное отклонение от среднего значения
                        # min, max - минимальное и максимальное значение
                        # 25%, 50%, 75% - Перцентиль (термин статистики)


#//////////////////////////////////////////////////////////////////////////
#=========================ПОСТРОЕНИЕ_ГРАФИКОВ==============================
#//////////////////////////////////////////////////////////////////////////
# https://stackoverflow.com/questions/64450497/scatterplot-do-not-show-any-graphs
# https://habr.com/ru/company/otus/blog/540526/

import seaborn as sns
import matplotlib.pyplot as plt

#=======================ТОЧЕЧНЫЕ_ГРАФИКИ_(ДИАГРАММА_РАССЕИВАНИЯ)===================

# sns.scatterplot(data=df, x='longitude', y='latitude') # строит карту домов из широты и долготы
# plt.show() # выводит график на экран

# sns.scatterplot(data=df, x='households', y='population', hue='totalRooms', size=10)
# plt.show()                                  # строит график зависимости кол-ва комнат от кол-ва семей
                                            # hue = столбец с изменяющимся цветом в зависимости от значения
                                            # size = размер точки hue на графике

# cols =['population', 'medianIncome', 'housingMedianAge', 'medianHouseValue']
# g = sns.PairGrid(df[cols])          # тут будет выведено (количество аргументов)^2
# g.map(sns.scatterplot)              # графиков со всем возможными отношениями
# plt.show()                          # X и Y (таблица графиков)

#==============================ЛИНЕЙНЫЕ_ГРАФИКИ===============================

# sns.relplot(x='latitude', y='medianHouseValue', kind='line', data=df)
# plt.show()

# sns.relplot(x='longitude', y='medianHouseValue', kind='line', data=df)
# plt.show()

#==============================ГИСТОГРАММА===============================

# sns.histplot(data=df, x='medianIncome') # гистограмма по доходам
# plt.show()

# sns.histplot(data=df, x='housingMedianAge')
# plt.show()

# sns.histplot(data=df[df['housingMedianAge'] > 50], x='medianIncome')
# plt.show() # доходы пожилых жителей

# df.loc[df['housingMedianAge'] <= 30, 'ageGroup'] = 'Young'
# df.loc[(df['housingMedianAge'] > 30) & (df['housingMedianAge'] <= 50), 'ageGroup'] = 'Middle old'
# df.loc[df['housingMedianAge'] > 50, 'ageGroup'] = 'Elderly'
# # print(df.columns) # добавим столбец ageGroup и заполним в зависимости от значения столбца housingMedianAge
# # print(df.head())
# df.groupby('ageGroup')['medianIncome'].mean().plot(kind='bar')
# plt.show() # средний доход по группам ageGroup

df.loc[df['medianIncome'] >= 6, 'incomeGroup'] = 'rich'
df.loc[df['medianIncome'] < 6, 'incomeGroup'] = 'bum'
# print(df.columns) # поделим на 2 группы в зависимости от состоятельности
# print(df.head())
sns.histplot(data=df, x='medianHouseValue', hue='incomeGroup')
plt.show() # покажем гистограмму по значению incomeGroup на фоне medianHouseValue
