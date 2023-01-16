

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# # Endowment task
# 
# Влияние гормонов на эффект владения
# 
# ![image](https://www.frontiersin.org/files/Articles/858168/fnins-16-858168-HTML-r3/image_m/fnins-16-858168-g001.jpg)


horm_df = pd.read_csv('horm_sort.csv', usecols = [0,1,2,3])
horm_df

#есть проблема с тем, что данные в последнем столбике должны быть числовыми, а они объект, как это исправить?
horm_df.info()

#приведем данные в последнем столбце к числовым, изначально они загрузились как текст
horm_df[['Testosterone']]= horm_df[['Testosterone']].apply(pd.to_numeric, errors='coerce')
horm_df

# ## Задание  1
# 
# В таблице приведены данные по каждому испытуемому до и после введения гормона (либо пласебо). Испытуемые те же самые, что и в задании с оценкой стоимости. 
# 
#  - Приведите таблицу к виду:
# 
# Subject| Testosterone_Time0_Type0| Testosterone_Time_1_type0| Testosterone_Time0_Type1| Testosterone_Time_1_type1| 
# 
# Сделайте это с помощью groupby и pivot_table


horm_df.columns

df2 = pd.pivot_table(horm_df, values=["Testosterone"], index = ['Subjects'] , columns=['Time','Type']).reset_index()
df2

df2.columns = ['_'.join(map(str, c)).strip('_') for c in df2]
df2.columns
df2

# - Проверьте все ли в порядке с данными, если есть пропуски обработайте их


df2.info()

df2 = df2.dropna()

# - Посчитайте процентное изменения уровня (100* (level1-level0)/level0) для обоих типов: type0 (пласебо), type1 (testosteron)


df2['placebo'] = (100 * ((df2.Testosterone_1_0 - df2.Testosterone_0_0) / df2.Testosterone_0_0))
df2['test'] = (100 * ((df2.Testosterone_1_1 - df2.Testosterone_0_1) / df2.Testosterone_0_1))
df2.round(2)

#  - Вычислите разницу в уровне гормона для каждого участника в состоянии пласебо и реального введения гормона: (Test(Time_1, type1) - Test(Time_1, type0)/Test(Time_1, type0)), назовите TPL_change


df2['TPL_change'] = ((df2.Testosterone_1_1 - df2.Testosterone_1_0) / df2.Testosterone_1_0); 
df2.round(2)

# - Нарисуйте график изменения уровня гормона после введения пласебо и реального. 


plot1 = df2.plot(x="Subjects", y=["Testosterone_0_0", "Testosterone_1_0"],figsize=(7, 7))
plot2 = df2.plot(x="Subjects", y=["Testosterone_0_1", "Testosterone_1_1"],figsize=(7, 7))
plot1
plot2

# сделайте табличку:
# код пациента в системе1 (где MR), в системе 2 (Subj), для каждого состояния (Placebo и введение гормона) будет свое значение  Tpl_change. То есть у вас должно появиться два новых столбика с показателями изменения гормонов 


df2['TPL_change_plac'] = ((df2.Testosterone_1_0 - df2.Testosterone_0_0) / df2.Testosterone_0_0); 
df2['TPL_change_horm'] = ((df2.Testosterone_1_1 - df2.Testosterone_0_1) / df2.Testosterone_0_1); 
df_fin = df2[['Subjects', 'TPL_change_plac', 'TPL_change_horm']]
df_fin.round(2)

# ## Задание 2
# 
# Смотрите справку в тетрадке GitGitHub
#  - Установить git локально
#  - с помощью командной строки сделать проект репозитория
#  - делаете три коммита:
#     - первый  - создаем файл1
#     - второй  - меняем файл1 и создаем файл2
#     - третий  - меняем файл1 и файл2 и создаем файл3
# Задание: научиться гулять между коммитами
# Задание: опубликовать проект на github




