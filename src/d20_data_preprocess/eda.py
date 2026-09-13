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
def showoutliers(df):
    numerical_features = df.select_dtypes(include=[np.number]).columns.tolist()
    for feature in numerical_features:
        plt.figure(figsize=(6,4))
        plt.title('BoxPlot')
        plt.boxplot(x=df[feature])
        plt.xlabel(feature)
        plt.show()
def d20help(topic="all"):
    
    catalog = {
        "Data Cleaning & Structuring": {
            "df.info()": "Prints a summary of the DataFrame, including data types and non-null counts.",
            "df.describe()": "Generates summary statistics like mean, median, and min/max for numerical columns.",
            "df.isna().sum()": "Counts the total number of missing (NaN) values in each column.",
            "df.dropna()": "Removes rows or columns that contain missing or null values.",
            "df.fillna()": "Replaces missing or null values with a specified value, mean, or median.",
            "df.drop_duplicates()": "Removes duplicate rows to ensure every record is unique.",
            "df.astype()": "Casts a column or Series to a specified data type (e.g., float to int).",
            "df.rename()": "Alters column or row labels using a dictionary mapping.",
            "df.drop()": "Removes specified rows or columns from the DataFrame."
        },
        "Data Transformation & Scaling": {
            "pd.get_dummies()": "Converts categorical text columns into one-hot encoded numerical variables.",
            "df.apply()": "Applies a custom function or lambda expression along a DataFrame axis.",
            "df.map()": "Maps values of a Series using a dictionary or function for label encoding.",
            "StandardScaler().fit_transform()": "Standardises features by removing the mean and scaling to unit variance.",
            "MinMaxScaler().fit_transform()": "Rescales numerical features to a specified range, typically 0 to 1.",
            "KBinsDiscretizer()": "Bins continuous numerical variables into discrete, categorical intervals."
        },
        "Reshaping & Combining Data": {
            "pd.concat()": "Combines multiple DataFrames or Series along a particular axis (rows or columns).",
            "pd.merge()": "Joins two DataFrames together based on a shared key or index (SQL-style join).",
            "df.groupby()": "Groups data by specific criteria to allow for aggregate calculations.",
            "df.pivot()": "Reshapes data from a long format to a wide format based on column values.",
            "df.melt()": "Unpivots a DataFrame from a wide format to a long format."
        },
        "Advanced Feature Engineering": {
            "train_test_split()": "Splits a dataset into random train and test subsets for model validation.",
            "SimpleImputer()": "A scikit-learn transformer to handle missing data using mean, median, or mode.",
            "OneHotEncoder()": "An ML-pipeline friendly scikit-learn transformer for encoding categorical features.",
            "LabelEncoder()": "Encodes target labels with numerical values between 0 and n-1 classes.",
            "PCA()": "Reduces dataset dimensionality by projecting data into a lower-dimensional space."
        }
    }

    # 2. Logic to handle the "all" argument
    if topic.lower() == "all":
        
        print("COMPLETE DATA PREPROCESSING REFERENCE GUIDES")
        
        
        for category, functions in catalog.items():
            print(f"\n🔹 {category}")
            print("-" * len(category))
            for func, desc in functions.items():
                # Formats the print to look clean in the console
                print(f"  • {func:<32} -> {desc}")
        print("\n" + "=" * 60)

    elif topic.lower() == 'clean':
        li=catalog["Data Cleaning & Structuring"]
        for func, desc in li.items():
            print(f"-{func:<10} -> {desc}")
    elif topic.lower() == 'transform':
        li=catalog["Data Transformation & Scaling"]
        for key,val in li.items():
            print(f"-{key:<10} -> {val}")
    elif topic.lower()=='reshape':
        li=catalog["Reshaping & Combining Data"]
        for key,val in li.items():
            print(f"-{key:<10} -> {val}")
    elif topic.lower()== 'advance':
        li=catalog["Advanced Feature Engineering"]
        for key,val in li.items():
            print(f"-{key:<10} -> {val}") 
    else:
        print(f"Topic '{topic}' not fully mapped yet. Pass 'all' to see all functions.")









