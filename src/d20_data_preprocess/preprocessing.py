import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import Image, display

def onehotenc(df,value:str):
    categorical_features = df.select_dtypes(include=[np.object_]).columns.tolist()
    # if(value!=null):
    df = pd.get_dummies(df,columns = [value],drop_first=True)
    return df
    # else:
    #     for feature in categorical_features:
    #         df = pd.get_dummies(df,columns = [feature],drop_first=True)
def levelenc(df,value:str):
    df[value]=df[value].map({True:1,False:0})
