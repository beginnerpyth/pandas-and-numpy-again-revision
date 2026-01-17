import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
pand=pd.read_csv('pand.csv')
#print(bios.head())
#print(pand.columns)
#print(bios.columns)#you need not to put the () its not callible
#print(pand.sort_values(['Pulse','Maxpulse'],ascending=True))#pulse and maxpulse value sorting through nuimbers
#print(pand.sort_values(['Pulse','Maxpulse'],ascending=(0,1)))#dont sort the pulse it is 0 but not the maxpulse it is 1 i.e true
#print(bios.info)
#print(bios.describe)
#print(bios.loc[0:10,'born_country'])#specific columna and rows and when you index it starts and ends exactly
#print(bios.iloc[0:3,1:5])#its the index locating so it works as python ends before
for index,row in pand.iterrows():
    print(index)
    print(row)
#print(bios.loc[bios['height_cm']>120,['name','born_city']])#locating values that only gives specific like name and borncity
#print(bios[bios['height_cm']>200][['name',"born_country"]])#another way to handle but remember that chossing specific column needs[[]]
#print(bios[bios["name"].str.contains('keith',case=False)])
#print(bios[(bios['height_cm']>150)&(bios['born_country']=='USA')])#conditionals#filtering data like numpy
#print(bios[bios['born_country'].isin(['USA','GBR'])&(bios['name'].str.startswith('Keith'))]) #filtering data
#print(bios.query('born_country=="USA"'))#another way to filter out the data
#print(bios.query('born_city=="Washington" and born_country=="USA"'))
