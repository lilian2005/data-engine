# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 12:36:09 2021

@author: ZhangYuanqi
"""


import pandas as pd
df=pd.read_csv('./car_complain.csv')
print(df)
#df.to_excel('./car_complain.xlsx', index=False)

df=df.drop('problem', axis=1).join(
    df["problem"].str.split(',',expand=True).stack().reset_index(
    level=1, drop=True).rename("problem"))
print(pd.isnull(df))
#df1=df.dropna(sebset=['problem'],inplace=True)
df=df.dropna(axis=0 ,how="any")
#df=df.fillna(0)
#print(df)
#df.to_excel('test.xls')
#输出的excel.test文件中确实显示有部分为空，可是为什么查出来都不为空， 我之前通过逗号拆分的problem列，逗号都去哪儿了？

 