import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier, plot_tree

# =========================================================
# 1. Criar a base de dados
# =========================================================

dados = pd.DataFrame({
    "estado_civil": [
        "Solteiro",
        "Casado",
        "Solteiro",
        "Divorciado",
        "Casado",
        "Solteiro",
        "Casado",
        "Divorciado",
        "Casado",
        "Solteiro"
    ],

    "renda_mensal": [
        2500,
        3200,
        3800,
        4500,
        5000,
        5500,
        6200,
        7000,
        8500,
        10000
    ],

    "aprovacao": [
        "Não",
        "Não",
        "Não",
        "Sim",
        "Não",
        "Sim",
        "Sim",
        "Sim",
        "Sim",
        "Sim"
    ]
})

print("Base de dados:")
print(dados)


# =========================================================
# 2. Separar variáveis preditoras e variável alvo
# =========================================================

X = dados[
    [
        "estado_civil",
        "renda_mensal"
    ]
]

y = dados["aprovacao"]


# =========================================================
# 3. Preparar a variável categórica
# =========================================================

# O estado civil precisa ser convertido para números.
# O OneHotEncoder cria uma coluna para cada categoria.

preprocessamento = ColumnTransformer(
    transformers=[
        (
            "estado_civil",
            OneHotEncoder(handle_unknown="ignore"),
            ["estado_civil"]
        ),
        (
            "renda",
            "passthrough",
            ["renda_mensal"]
        )
    ]
)


# =========================================================
# 4. Criar a árvore de decisão
# =========================================================

arvore = DecisionTreeClassifier(
    criterion="gini",
    random_state=42
)


# =========================================================
# 5. Criar o pipeline
# =========================================================

modelo = Pipeline(
    steps=[
        ("preprocessamento", preprocessamento),
        ("arvore", arvore)
    ]
)


# =========================================================
# 6. Treinar o modelo
# =========================================================

modelo.fit(X, y)

print("\nModelo treinado com sucesso.")


# =========================================================
# 7. Recuperar os nomes das variáveis após transformação
# =========================================================

encoder = modelo.named_steps[
    "preprocessamento"
].named_transformers_[
    "estado_civil"
]

nomes_estado_civil = encoder.get_feature_names_out(
    ["estado_civil"]
)

nomes_variaveis = list(nomes_estado_civil) + [
    "renda_mensal"
]

print("\nVariáveis utilizadas pela árvore:")
print(nomes_variaveis)


# =========================================================
# 8. Plotar a árvore
# =========================================================

plt.figure(figsize=(14, 8))

plot_tree(
    modelo.named_steps["arvore"],
    feature_names=nomes_variaveis,
    class_names=modelo.named_steps["arvore"].classes_,
    filled=True,
    rounded=True,
    impurity=True,
    proportion=False,
    precision=3
)

plt.title(
    "Árvore de Decisão - Aprovação de Empréstimo"
)

plt.show()


# =========================================================
# 9. Verificar a classificação da própria base
# =========================================================

previsoes = modelo.predict(X)

dados["previsao_modelo"] = previsoes

print("\nResultado das previsões:")
print(dados)


# =========================================================
# 10. SIMULAÇÃO DE UM NOVO CLIENTE
# =========================================================

novo_cliente = pd.DataFrame({
    "estado_civil": [
        "Divorciado",
    ],

    "renda_mensal": [
        200
    ]
})

resultado = modelo.predict(
    novo_cliente
)

print("\nNovo cliente:")
print(novo_cliente)

print(
    "\nResultado da análise:",
    resultado[0]
)


# =========================================================
# 11. Probabilidade prevista
# =========================================================

probabilidades = modelo.predict_proba(
    novo_cliente
)

classes = modelo.named_steps[
    "arvore"
].classes_

print("\nProbabilidades:")

for classe, probabilidade in zip(
    classes,
    probabilidades[0]
):
    print(
        f"{classe}: "
        f"{probabilidade * 100:.2f}%"
    )
