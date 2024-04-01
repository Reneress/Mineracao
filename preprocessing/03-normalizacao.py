import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import IPython.display as display
import seaborn as sns
import math
import warnings

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
    
   

    # # Z-score normalization
    x_zcore = StandardScaler().fit_transform(x)
    normalized1Df = pd.DataFrame(data = x_zcore, columns = features)
    normalized1Df = pd.concat([normalized1Df, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalized1Df,"Dataframe Z-Score Normalized")

    # Mix-Max normalization
    x_minmax = MinMaxScaler().fit_transform(x)
    normalized2Df = pd.DataFrame(data = x_minmax, columns = features)
    normalized2Df = pd.concat([normalized2Df, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalized2Df,"Dataframe Min-Max Normalized")
 
 
 #--------------------------------------------------------------
    #minmax Narmalizartion dfAlter
    x_minmax = MinMaxScaler().fit_transform(xAlter)
    normalized3Df = pd.DataFrame(data = x_minmax, columns = features)
    normalized3Df = pd.concat([normalized3Df, dfAlter[[target]]], axis = 1)
    ShowInformationDataFrame(normalized3Df,"Dataframe Min-Max Normalized")
    print(normalized3Df.columns.values.tolist())
     
    # plt.figure(figsize=(20,12))
    # sns.heatmap(normalized3Df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=2)
    # plt.title('Correlation matrix')
    # plt.show()
    # #Plotando a matriz de correlação com a coluna target alterada
    
    # # PCA projection
    # warnings.filterwarnings("ignore")
    # cols1 = ['Marital status','Application mode','Application order','Course','Daytime/evening attendance	','Previous qualification',
    #             'Previous qualification (grade)','Nacionality',"Mother's qualification","Father's qualification","Mother's occupation",
    #             "Father's occupation",'Admission grade','Displaced','Educational special needs','Debtor','Tuition fees up to date',
    #             'Gender','Scholarship holder','Age at enrollment','International','Curricular units 1st sem (credited)',
    #             'Curricular units 1st sem (enrolled)','Curricular units 1st sem (evaluations)','Curricular units 1st sem (approved)',
    #             'Curricular units 1st sem (grade)','Curricular units 1st sem (without evaluations)','Curricular units 2nd sem (credited)',
    #             'Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)',
    #             'Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP']
    # cols2=['Tuition fees up to date','Curricular units 1st sem (approved)','Curricular units 1st sem (grade)',
    #           'Curricular units 2nd sem (approved)','Curricular units 2nd sem (grade)']
    # for col in cols1:
    #     print(f"\n{dfAlter[col].value_counts()}")
    #     print('_'*25)
        
    # # plotando gráfico de características relacionando com Target
    # plt.figure (figsize = (12 , 10) , dpi = 100)
    # heatmap = sns.heatmap (dfAlter.corr()[['Target']].sort_values (by = 'Target', ascending = False), vmin = -1, vmax = 1, annot = True, cmap = 'GnBu')
    # heatmap.set_title ('Features Correlating with Target', fontdict = {'fontsize':12} , pad = 18)
    # plt.show()

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n") 



if __name__ == "__main__":
    main()