import pickle
from scipy import stats
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
 
# Para exibição sem truncar
pd.set_option('display.expand_frame_repr', False)
 
# ===== 1) Carregar dados =====
database = pd.read_excel('HR_Abandono.xlsx', sheet_name='HR_Abandono')
 
# ===== 2) EDA rápida =====
print(database.head(10))
print("-------------------")
print(database.tail(10))
print("-------------------")
print(database.min(numeric_only=True))
print("-------------------")
print(database.max(numeric_only=True))
print("*****************")
print(database.dtypes)
 
# ===== 3) Verificar valores nulos =====
print("\nNulos por coluna:")
print(database.isnull().sum())
 
# ===== 4) Verificar valores negativos =====
numericas = database.select_dtypes(include='number')
negativos = database[(numericas < 0).any(axis=1)]
print("\nLinhas com algum valor negativo:")
print(negativos)
 
# Estatísticas antes da remoção de outliers
print("\nEstatísticas antes da remoção de outliers:")
print(database.describe(include='all'))

z = np.abs(stats.zscore(database['average_montly_hours']))

idx_cols = database.index[z>3]

print(idx_cols)

database = database.drop(idx_cols)
print(database.describe(include='all'))

y = database['left']
X = database.drop(columns=['left', 'id'])

cat_cols = list(X.select_dtypes(include=['object', 'category']).columns)
print('Colunas categóricas:')
print(cat_cols)

num_cols = list(X.select_dtypes(include=['number']).columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)

preprocess = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), cat_cols),
    ]
)

X_train = preprocess.fit_transform(X_train)
X_test = preprocess.transform(X_test)

with open('hr_turnover.pkl', 'wb') as f:
    pickle.dump(
        {
            'X_train': X_train,
            'y_train': y_train,
            'X_test': X_test,
            'y_test': y_test,
            'preprocess': preprocess
        }, f
    )

print("\nArquivo salvo: hr_turnover.pkl")