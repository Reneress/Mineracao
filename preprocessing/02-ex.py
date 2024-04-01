import pandas as pd
import numpy as np
from ucimlrepo import fetch_ucirepo 

def main():
    # Faz a leitura do arquivo
    names = ['Marital status','Application mode',	'Application order',	'Course',	'Daytime/evening attendance',	'Previous qualification',
    'Previous qualification (grade)',	'Nacionality',	'Mothers qualification',	'Fathers qualification', 'Mothers occupation',	
    'Fathers occupation',	'Admission grade',	'Displaced', 'Educational special needs',	'Debtor',	'Tuition fees up to date',	'Gender','Scholarship holder',	
    'Age at enrollment',	'International',	'Curricular units 1st sem (credited)',	'Curricular units 1st sem (enrolled)',	'Curricular units 1st sem (evaluations)',	
    'Curricular units 1st sem (approved)',	'Curricular units 1st sem (grade)',	'Curricular units 1st sem (without evaluations)',	'Curricular units 2nd sem (credited)',
    'Curricular units 2nd sem (enrolled)',	'Curricular units 2nd sem (evaluations)',	'Curricular units 2nd sem (approved)',	'Curricular units 2nd sem (grade)',	
    'Curricular units 2nd sem (without evaluations)',	'Unemployment rate',	'Inflation rate',	'GDP',	'Target'] 
    
    features = ['Marital status','Application mode','Application order','Course','Daytime/evening attendance	','Previous qualification',
                'Previous qualification (grade)','Nacionality',"Mother's qualification","Father's qualification","Mother's occupation",
                "Father's occupation",'Admission grade','Displaced','Educational special needs','Debtor','Tuition fees up to date',
                'Gender','Scholarship holder','Age at enrollment','International','Curricular units 1st sem (credited)',
                'Curricular units 1st sem (enrolled)','Curricular units 1st sem (evaluations)','Curricular units 1st sem (approved)',
                'Curricular units 1st sem (grade)','Curricular units 1st sem (without evaluations)','Curricular units 2nd sem (credited)',
                'Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)',
                'Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP']
    output_file = '../Base/alterations/dataC.csv'
    input_file = '../Base/alterations/dataAlter.csv'
    df = pd.read_csv(input_file,         # Nome do arquivo com dados
                     sep=";",
                     #names = names,      # Nome das colunas 
                     #usecols = features, # Define as colunas que serão  utilizadas
                    )      # Define que ? será considerado valores ausentes
    


    
    df_original = df.copy()
    # Imprime as 15 primeiras linhas do arquivo
    print("PRIMEIRAS 15 LINHAS\n")
    print(df.head(15))
    print("\n")        

    # Imprime informações sobre dos dados
    print("INFORMAÇÕES GERAIS DOS DADOS\n")
    print(df.info())
    print("\n")
    
    # Imprime uma analise descritiva sobre dos dados
    print("DESCRIÇÃO DOS DADOS\n")
    print(df.describe())
    print("\n")
    
    # Imprime a quantidade de valores faltantes por coluna
    print("VALORES FALTANTES\n")
    print(df.isnull().sum())
    print("\n")    
    
    columns_missing_value = df.columns[df.isnull().any()]
    print(columns_missing_value)
    method = 'mode' # number or median or mean or mode
    
    for c in columns_missing_value:
        UpdateMissingValues(df, c)
    
    print(df.describe())
    print("\n")
    print(df.head(15))
    print(df_original.head(15))
    print("\n")
    
    # Salva arquivo com o tratamento para dados faltantes
    df.to_csv(output_file, header=True, index=False)  
    

def UpdateMissingValues(df, column, method="mode", number=0):
    if method == 'number':
        # Substituindo valores ausentes por um número
        df[column].fillna(number, inplace=True)
    elif method == 'median':
        # Substituindo valores ausentes pela mediana 
        median = df[column].median()
        df[column].fillna(median, inplace=True)
    elif method == 'mean':
        # Substituindo valores ausentes pela média
        mean = df[column].mean()
        df[column].fillna(mean, inplace=True)
    elif method == 'mode':
        # Substituindo valores ausentes pela moda
        mode = df[column].mode()[0]
        df[column].fillna(mode, inplace=True)


if __name__ == "__main__":
    main()