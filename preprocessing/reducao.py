import pandas as pd
import numpy as np

# Suponha que df é o seu DataFrame
df = pd.read_csv('../Base/alterations/data03.csv',sep=",") # Substitua isso pelo seu DataFrame real

# Suponha que 'target' é a coluna alvo
target = 'Target'  # Substitua isso pela sua coluna alvo real

# Faça uma cópia do DataFrame original
df_copy = df.copy()

# Calcule a correlação de cada coluna com a coluna alvo
corr_with_target = df_copy.corr()[target].abs()

# Encontre as colunas com correlação menor que 0.3 com a coluna alvo
to_drop = [column for column in corr_with_target.index if corr_with_target[column] < 0.2]

# Remova as colunas
df_copy.drop(to_drop, axis=1, inplace=True)

# Salve a nova versão do DataFrame em um arquivo CSV
df_copy.to_csv('../Base/alterations/dataRedux.csv', index=False)

