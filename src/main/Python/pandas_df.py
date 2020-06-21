import pandas as pd
import os
cwd=os.getcwd()
print(cwd)
BASE_DIR=os.path.dirname("C:\\retail_db\\data-master\\retail_db\\")
#print(cwd)
#data_file=(C://retail_db//data-master//retail_db/orders)
#C:\retail_db\data-master\retail_db\orders

#pd.DataFrame
df=os.path.join(BASE_DIR, 'orders')
              # .dirname()"C://retail_db//data-master//retail_db/orders")
for filename in os.listdir(df):
    print(filename)
#df1=pd.read_csv(os.path.dirname("C://retail_db//data-master//retail_db//"),"part-00000")
df1=pd.read_csv("part-00000")
print(df.head())
print(df1.count())
