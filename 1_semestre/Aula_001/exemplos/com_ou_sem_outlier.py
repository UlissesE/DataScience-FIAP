import pandas as pd

com_outlier = pd.Series([120, 130, 125, 128, 122, 600])
sem_outlier = pd.Series([120, 130, 125, 128, 122])

def resumo(x):
    return {
        "media":x.mean(),
        "mediana": x.median(),
        "var_amostral": x.var(ddof=1),
        "dp_amostral": x.std(ddof=1)
    }

print("Com outlier: ", resumo(com_outlier))
print("Sem outlier: ", resumo(sem_outlier))