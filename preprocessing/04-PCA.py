import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


def main():
        
    
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
    
    # features=['Tuition fees up to date','Curricular units 1st sem (approved)','Curricular units 1st sem (grade)',
    #           'Curricular units 2nd sem (approved)','Curricular units 2nd sem (grade)']
    
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     sep=","
                     ) # Nome das colunas 
                  
    ShowInformationDataFrame(df,"Dataframe original")

    # Separating out the features
    x = df.loc[:, features].values

    # Separating out the target
    y = df.loc[:,[target]].values

    # #Standardizing the features
    # x = StandardScaler().fit_transform(x)
    # normalizedDf = pd.DataFrame(data = x, columns = features)
    # normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
    # ShowInformationDataFrame(normalizedDf,"Dataframe Normalized")

    # Z-score normalization
    # x = StandardScaler().fit_transform(x)
    # normalizedDf = pd.DataFrame(data = x, columns = features)
    # normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
    # ShowInformationDataFrame(normalizedDf,"Dataframe Z-Score Normalized")
    
     # Mix-Max normalization
    x = MinMaxScaler().fit_transform(x)
    normalizedDf = pd.DataFrame(data = x, columns = features)
    normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalizedDf,"Dataframe Min-Max Normalized")
    
    
    # PCA projection
    pca = PCA(n_components=3)    
    principalComponents = pca.fit_transform(x)
    print("Explained variance per component:")
    print(pca.explained_variance_ratio_.tolist())
    print("\n\n")
    
    # --------------------------------------------------- 3D

    principalDf = pd.DataFrame(data = principalComponents[:,0:3], 
                               columns = ['principal component 1', 
                                          'principal component 2',
                                          'principal component 3'])
    finalDf = pd.concat([principalDf, df[[target]]], axis = 1)    
    ShowInformationDataFrame(finalDf,"Dataframe PCA")
    
    VisualizePcaProjection(finalDf, target)


def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
           
def VisualizePcaProjection(finalDf, targetColumn):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(111, projection='3d') 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_zlabel('Principal Component 3', fontsize = 15)
    ax.set_title('3 component PCA', fontsize = 20)
    targets = ["Dropout", "Enrolled","Graduate" ]
    colors = ['r', 'g', 'b']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   finalDf.loc[indicesToKeep, 'principal component 3'],
                   c = color, s = 50)
    ax.legend(targets)
    ax.grid()
    plt.show()
    
    # ------------------------------ 2D
    
#     principalDf = pd.DataFrame(data = principalComponents[:,0:2], 
#                                columns = ['principal component 1', 
#                                           'principal component 2'])
#     finalDf = pd.concat([principalDf, df[[target]]], axis = 1)    
#     ShowInformationDataFrame(finalDf,"Dataframe PCA")
    
#     VisualizePcaProjection(finalDf, target)


# def ShowInformationDataFrame(df, message=""):
#     print(message+"\n")
#     print(df.info())
#     print(df.describe())
#     print(df.head(10))
#     print("\n")
    
           
# def VisualizePcaProjection(finalDf, targetColumn):
#     fig = plt.figure(figsize = (8,8))
#     ax = fig.add_subplot(1,1,1) 
#     ax.set_xlabel('Principal Component 1', fontsize = 15)
#     ax.set_ylabel('Principal Component 2', fontsize = 15)
#     ax.set_title('2 component PCA', fontsize = 20)
#     targets = ["Dropout", 'Enrolled',"Graduate" ]
#     colors = ['r', 'g', 'b']
#     for target, color in zip(targets,colors):
#         indicesToKeep = finalDf[targetColumn] == target
#         ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
#                    finalDf.loc[indicesToKeep, 'principal component 2'],
#                    c = color, s = 50)
#     ax.legend(targets)
#     ax.grid()
#     plt.show()


if __name__ == "__main__":
    main()