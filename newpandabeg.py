import pandas as pd
pand=pd.DataFrame([[8,6,5,45],[2,3,4,5,6],[23,54,67,7,5]],columns=['A','B','C','D','E'],index=[0,1,2])
print(pand)
sand=pd.read_csv('pand.csv')
#print(sand)
print(sand.head(2))
#print(sand.tail(2))
#print(sand.index)
print(sand.sample(3))
print(sand.sample(3,random_state=1))
print(sand.nunique())
print(sand['Pulse'].nunique())
print(sand.loc[1])
print(sand.loc[1:3,["Pulse"]])
print(sand.iloc[0:2,[0,3]])
#sand.index=sand['Pulse']
#print(sand)# to make the data index and pilse the same thing

#to cahnge the value we can do the specific method 
sand.loc[0,['Pulse']]=12
print(sand.head(1))
