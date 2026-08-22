import numpy as np
import pandas as pd
import plt

# Expande o pd.describe para exibir todas as colunas
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_columns', None)

dataframe = pd.read_excel("data/raw/HR_Abandono_1.xlsx")

print(dataframe.describe())

# print(dataframe.groupby('left')['satisfaction_level'].mean())
# print(dataframe.groupby('left')['satisfaction_level'].median())
# print(dataframe.groupby('left')['satisfaction_level'].std())
print()
print('==================================')
print('Níveis de satisfação para saída')
print('==================================')
print()
print(dataframe.groupby('left')['satisfaction_level'].agg(['mean', 'median', 'std']))

print()
print()

print("numero de nulos: ", dataframe.isnull().sum().sum())
print()


# print('==================================')
# print('Promoções para saída')
# print('==================================')
# print()
# print(dataframe.groupby('left')['promotion_last_5years'].agg(['mean', 'median', 'std']))
#
# print()
# print()
#
# print('==================================')
# print('Tempo de empresa para saída')
# print('==================================')
# print()
# print(dataframe.groupby('left')['time_spend_company'].agg(['mean', 'median', 'std']))
#
# print()
# print()
#
# print('==================================')
# print('Saída para departamento')
# print('==================================')
# print()
# print(dataframe.groupby('depto')['left'].agg(['mean', 'median', 'std']))
#
# print()
# print()
#
# print('==================================')
# print('Acidentes para saída')
# print('==================================')
# print()
# print(dataframe.groupby('left')['Work_accident'].agg(['mean', 'median', 'std']))


if 'left' in dataframe.columns:
    plt.hist(dataframe['left'])
    plt.title('Histograma de numeros de left (saida)')
    plt.xlabel('Numero de left')
    plt.ylabel('Frequencia')
    plt.show()

for col in dataframe.columns:
    plt.hist(dataframe[col])
    plt.title('Histograma de {} '.format(col))
    plt.xlabel('Numero de left')
    plt.ylabel('Frequencia')
    plt.show()