import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def alteraTarget(row):
    if row['Target'] == "Graduate":
        return 1
    elif row['Target'] == "Enroled":
        return 0
    else:
        return -1
    
def main():
    # Faz a leitura do arquivo
    input_file = '../Base/alterations/data03.csv'
    
    features = ['Marital status','Application mode','Application order','Course','Daytime/evening attendance	','Previous qualification',
                'Previous qualification (grade)','Nacionality',"Mother's qualification","Father's qualification","Mother's occupation",
                "Father's occupation",'Admission grade','Displaced','Educational special needs','Debtor','Tuition fees up to date',
                'Gender','Scholarship holder','Age at enrollment','International','Curricular units 1st sem (credited)',
                'Curricular units 1st sem (enrolled)','Curricular units 1st sem (evaluations)','Curricular units 1st sem (approved)',
                'Curricular units 1st sem (grade)','Curricular units 1st sem (without evaluations)','Curricular units 2nd sem (credited)',
                'Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)',
                'Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP']
    target = 'Target'
    output_file = '../Base/alterations/dataAlter.csv'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     sep=","
                     ) # Nome das colunas 
                         
    # ShowInformationDataFrame(df,"Dataframe original")
  #----------------------------------------------------------------  
    dfAlter = pd.read_csv('../Base/alterations/dataAlter.csv',sep=",")
    ShowInformationDataFrame(dfAlter,"Dataframe alterado")
    
    #É necessário alterar a coluna target para numérica
    xAlter = dfAlter.loc[:, features].values
    yAlter = dfAlter.loc[:,[target]].values
#--------------------------------------------------------------- 
    #Separating out the features
    x = df.loc[:, features].values
    # Separating out the target
    y = df.loc[:,[target]].values
    
     #ver as distribuições de maneira clara Grafico Quantis
    columns = ['Marital status','Curricular units 1st sem (credited)',
                'Curricular units 1st sem (enrolled)','Curricular units 1st sem (evaluations)','Curricular units 1st sem (approved)',
                'Curricular units 1st sem (grade)','Curricular units 1st sem (without evaluations)','Curricular units 2nd sem (credited)',
                'Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)',
                'Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP']
    palette ="GnBu"
    # for column in columns:
    #     plt.figure(figsize=(15,2))
    #     sns.boxplot(x=df[column], palette=palette)
    #     plt.title(column)
    #     stats = dfAlter[column].describe()
    #     stats_text = ", ".join([f"{key}: {value:.2f}" for key, value in stats.items()])
    #     print(f"\n{column} Statistics:\n{stats_text}")
    #     plt.show()
        
    # import seaborn as sns

    # df_dispersao =df[['Curricular units 1st sem (grade)', atributo]]
    # df_dispersao = df_dispersao.groupby(['Curricular units 1st sem (grade)',atributo]).size().reset_index(name="tamanho")
    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1.5,1.5])

    # ax = sns.scatterplot(data=df_dispersao, x='Class-Name', y = atributo, size="tamanho", legend=False, sizes=(1000,10000))
    # plt.show()
    
    
    #ver as distribuições de maneira clara
    columns=['Marital status','Curricular units 2nd sem (credited)',
                'Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)',
                'Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP' ]
    palette ="GnBu"
    for column in columns:
        plt.figure(figsize=(15,2))
        sns.violinplot(x=dfAlter[column], palette=palette)
        plt.title(column)
        plt.show()

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n") 



if __name__ == "__main__":
    main()