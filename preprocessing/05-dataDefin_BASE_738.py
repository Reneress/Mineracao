import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import IPython.display as display
import seaborn as sns
import math
import warnings

    

def main():
        
    
    input_file = '../Base/alterations/data03.csv'
    
    # features = ['Marital status','Application mode','Application order','Course','Daytime/evening attendance','Previous qualification',
    #             'Previous qualification (grade)','Nacionality',"Mother's qualification","Father's qualification","Mother's occupation",
    #             "Father's occupation",'Admission grade','Displaced','Educational special needs','Debtor','Tuition fees up to date',
    #             'Gender','Scholarship holder','Age at enrollment','International','Curricular units 1st sem (credited)',
    #             'Curricular units 1st sem (enrolled)','Curricular units 1st sem (evaluations)','Curricular units 1st sem (approved)',
    #             'Curricular units 1st sem (grade)','Curricular units 1st sem (without evaluations)','Curricular units 2nd sem (credited)',
    #             'Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)',
    #             'Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP']
    target = 'Target'
    
    features=['Tuition fees up to date','Curricular units 1st sem (approved)','Curricular units 1st sem (grade)',
              'Curricular units 2nd sem (approved)','Curricular units 2nd sem (grade)']
    
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     sep=","
                     ) # Nome das colunas 
                  
    # ShowInformationDataFrame(df,"Dataframe original")

   #----------------------------------------------------------------  
    dfAlter = pd.read_csv('../Base/alterations/dataAlter.csv',sep=",")
   
    # ShowInformationDataFrame(dfAlter,"Dataframe alterado")
#---------------------------------------------------------------

   
    Gender = df['Gender'].value_counts()
    Gender.plot(kind='barh', color = ['red', 'blue'])
    plt.xlabel('Quantidade de alunos')
    plt.ylabel('0 = Feminino, 1 = Masculino')
    plt.title('Gênero')
    plt.show()

    Bolsista = df['Scholarship holder'].value_counts()
    # Bolsista.plot(kind='barh', color = ['red', 'Green'])
    Bolsista.plot(kind='pie', autopct='%1.2f%%')
    plt.xlabel('Quantidade de alunos')
    plt.ylabel('0 = Não Bolsista, 1 = Bolsista')
    plt.title('Bolsista')
    plt.show()
    
    Bolsista = df['Educational special needs'].value_counts()
    # Bolsista.plot(kind='barh', color = ['red', 'Green'])
    Bolsista.plot(kind='pie', autopct='%1.2f%%')
    plt.xlabel('Quantidade de alunos')
    plt.ylabel('1 = Com necessidade especiais, 0 = Sem necessidades especiais')
    plt.title('Educação especial')
    plt.show()

    Target = dfAlter['Target'].value_counts()

    plt.figure(figsize=(6,6))
    plt.pie(Target, labels = Target.index, colors = ['red', 'green', 'blue'], autopct='%1.1f%%')
    plt.xlabel('Quantidade de alunos')
    plt.ylabel('Classificação')
    plt.title('Target')
    plt.show()
# Exibição do g
    
    
    # sns.distplot(df['Previous qualification'], kde=True, bins=10)
    # # df['Previous qualification'].plot(kind='density')
    # plt.xlabel('Previous qualification')
    # plt.ylabel('Quantidade de alunos')
    # plt.show()
    
    

    # df_c=['Previous qualification',
    #             'Previous qualification (grade)','Admission grade','Displaced','Scholarship holder','Curricular units 1st sem (approved)',
    #             'Curricular units 1st sem (grade)','Curricular units 2nd sem (approved)',
    #             'Curricular units 2nd sem (grade)','Inflation rate','GDP']  
    # for i in df_c:
    #     sns.set_theme(style="white")
    #     g = sns.JointGrid(data=dfAlter, x=i,y='Target',space=0)
    #     g.plot_joint(sns.kdeplot,fill=True,thresh=0, levels=100, cmap="GnBu")
    #     g.plot_marginals(sns.histplot, color="#52796f", alpha=1, bins=20)
    #     plt.show()
        
    # df_categorical = df[['Marital status','Application mode','Application order','Course','Daytime/evening attendance	','Previous qualification',
    #             'Previous qualification (grade)','Nacionality',"Mother's qualification","Father's qualification","Mother's occupation",
    #             "Father's occupation",'Admission grade','Displaced','Educational special needs','Debtor','Tuition fees up to date',
    #             'Gender','Scholarship holder','Age at enrollment','International','Curricular units 1st sem (credited)',
    #             'Curricular units 1st sem (enrolled)','Curricular units 1st sem (evaluations)','Curricular units 1st sem (approved)',
    #             'Curricular units 1st sem (grade)','Curricular units 1st sem (without evaluations)','Curricular units 2nd sem (credited)',
    #             'Curricular units 2nd sem (enrolled)','Curricular units 2nd sem (evaluations)','Curricular units 2nd sem (approved)',
    #             'Curricular units 2nd sem (grade)','Curricular units 2nd sem (without evaluations)','Unemployment rate','Inflation rate','GDP']].astype(str)

# todas as colunas só para comparar com as categoricas que vou dropar


    # df_numerical = df.drop(df_categorical.columns, axis=1)

    # fig=plt.figure(figsize=(30,18))
    # for i,col in enumerate(df_numerical):
    #     if i==15:
    #         break
    #     ax=fig.add_subplot(5, 3,(i+1))
    #     sns.scatterplot(x='ram',y=col,hue='Target',data=dfAlter,palette="tab10")
        
def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    

if __name__ == "__main__":
    main()