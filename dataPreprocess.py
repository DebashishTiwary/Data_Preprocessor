import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import Image, display

#entering csv file
def EDA(df,target:any):
    #check the extension of data
    #print(df[target])
    # print("Your Target Column:")
    # print(df[target])
    # print('-------------------------------------------------------------------------------------')
    print("Data Size")
    print(df.shape)
    print("Information:")
    print(df.info())
    print('-------------------------------------------------------------------------------------')
    print("Data Description:")
    print(df.describe())
    print('-------------------------------------------------------------------------------------')
    print("Null Values:")
    print(df.isnull().sum())
    # print('-------------------------------------------------------------------------------------')
    plt.figure(figsize=(8,6))
    plt.title("Heatmap")
    sns.heatmap(df.corr(numeric_only=True),annot=True,cmap='coolwarm')
    print('-------------------------------------------------------------------------------------')
    
    numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = df.select_dtypes(include=[np.object_]).columns.tolist()
    print("Numerical Features:{}".format(numerical_features))
    print("Categorical Features:{}".format(categorical_features))
    print('-------------------------------------------------------------------------------------')
    for feature in numerical_features:
        plt.figure(figsize=(6, 4))
        plt.title('BoxPlot')
        sns.histplot(df[feature], kde=True,bins=10)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.show()

    for feature in numerical_features:
        plt.figure(figsize=(6,4))
        plt.title('BoxPlot')
        plt.boxplot(x=df[feature])
        plt.xlabel(feature)
        plt.show()



