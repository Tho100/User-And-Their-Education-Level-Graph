import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import os
import warnings
# ! Upload this to repos
warnings.filterwarnings('ignore')

data = pd.read_excel("C:\\users\\HP\\Documents\\Datascience task\\Person.xlsx")

# Education level section

education = data['Education'].head(6) # - 1
first_name = data['First Name'].head(6) # - 1 
sns.set_theme()
sns.stripplot(first_name,education,data=data)
data.head(5)
