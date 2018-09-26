import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Data importing (we will use data from Pandas Case Study)
cust_data = pd.read_csv("C:/Users/ChandraMouli/Desktop/Pandas Case Study/Cust_data.csv")
cust_demo = pd.read_csv("C:/Users/ChandraMouli/Desktop/Pandas Case Study/Cust_demo.csv")
cust_new  = pd.read_csv("C:/Users/ChandraMouli/Desktop/Pandas Case Study/cust_new.csv")
# Data Understanding
print cust_data.head(5)
print cust_demo.head(5)
print cust_new.head(5)
import numpy as np
cust_demo.select_dtypes(include = ['object', 'floating'] ).head(5)
Data Manipulation

Sub Setting Data
cust_data.columns
cust_data[['ID','RevolvingUtilization', 'MonthlyIncome']].head(5)
cust_data.iloc[[1,2,10,20],[2,3,5,7]]
(cust_data.SeriousDlqin2yrs==0) & (cust_data.RevolvingUtilization>0.5)
cust_data[(cust_data.SeriousDlqin2yrs==0) & (cust_data.RevolvingUtilization>0.5) ]
#subsetting data
cust_data[["ID", "DebtRatio"]].head(2)
#Creating new Columns variable No_of_30_Plus_DPD =  No_of_30_59_DPD + No_of_60_89_DPD + No_of_90_DPD
cust_data['No_of_30_Plus_DPD'] = cust_data['No_of_30_59_DPD']+cust_data['No_of_60_89_DPD']+cust_data['No_of_90_DPD']
cust_data.head(2)
#dropping columns
cust_data1.drop('MonthlySavings1', axis=1).head(2) # it creates new data
#cust_data.drop('monthly_savings', inplace=True, axis=1) # it modify the existing data
cust_data.head(2)
##Bining of data
cust_data1['MonthlyIncome'].head(10)
pd.cut(cust_data1['MonthlyIncome'],3, labels = ['0-33', '33-66','66-100']).head(10)
#renaming column "RevolvingUtilization with Rev_Utilization" and "SeriousDlqin2yrs with SeriousDlq"
print cust_data1.columns
cust_data1=cust_data1.rename(columns={'RevolvingUtilization':'Rev_Utilization', 'SeriousDlqin2yrs':'SeriousDlq'}).head(10)
## Sorting the data
cust_data.sort_values(by='MonthlyIncome', ascending=False).head(10)
##Handling Duplicates
cust_data.head(5)
sum(cust_demo.duplicated())
#handling missing values
s12 = cust_data['MonthlyIncome']
# Detect missing values
zip(s12, s12.isnull(), s12.notnull())
print sum(s12.isnull())

s13=s12.fillna(s12.mean()
sum(s13.isnull())
# Replace missing values with 0
s12.fillna(0)
# Fill with median
s12.fillna(s12.median())
# dropping the observations
s12.dropna()
##Data Manipulation
cust_data.columns
cust_demo.columns
cust_demo[['Gender', 'age']].groupby('Gender').mean()
grouped = cust_data[['RevolvingUtilization','SeriousDlqin2yrs']].groupby('SeriousDlqin2yrs')
print type(grouped)
pd.DataFrame(pd.concat([grouped.max(), grouped.min(), grouped.mean(), grouped.std()], axis=1).values,
          columns=['Max', 'Min', 'Mean', 'Stddev'])
import pandas as pd
pd.DataFrame(pd.concat([g.max(), g.min(), g.sum(), g.mean(), g.median(), g.std()], axis=1).values, 
             columns=['Max', 'Min', 'sum','avg', 'median', 'std'])
