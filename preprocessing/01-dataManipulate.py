import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

def alteraTarget(row):
    if row['Target'] == "Graduate":
        return 2
    elif row['Target'] == "Enrolled":
        return 1
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
    output_file1 = '../Base/alterations/data03.csv'
    output_file2 = '../Base/alterations/dataAlter.csv'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     sep=","
                     ) # Nome das colunas 
                         
    ShowInformationDataFrame(df,"Dataframe original")
    
    dfNorm = df.copy()
    df["Curricular units 1st sem (grade)"] = df["Curricular units 1st sem (grade)"].astype('int64')
    df["Curricular units 2nd sem (grade)"] = df["Curricular units 2nd sem (grade)"].astype('int64')
    ShowInformationDataFrame(dfNorm,"Dataframe Alterado 1")
    dfNorm.to_csv(output_file1,header=True, index=False)
    
  #----------------------------------------------------------------  
    dfAlter = dfNorm.copy()
    dfAlter['Target'] = dfAlter.apply(alteraTarget, axis=1)
    ShowInformationDataFrame(dfAlter,"Dataframe alterado 2")
    dfAlter.to_csv(output_file2, header=True, index=False)
    
#_______________DataFrame Alterado__________________________________

    

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n") 



if __name__ == "__main__":
    main()