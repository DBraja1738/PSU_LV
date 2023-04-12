import pandas as pd
import numpy as np

mtcars= pd.read_csv('mtcars.csv')
print(mtcars)
#1
mtcars=mtcars.sort_values(by='mpg',ascending=False)
#print(mtcars[0:5])
#2
#print(mtcars[mtcars.cyl==8].head(3))
#3
#mtcars_mean=mtcars[mtcars.cyl==6].mean()

#print(mtcars_mean.mpg)
#4
mtcars_4cyl=mtcars[(mtcars.cyl==4) & (mtcars.wt>2000) & (mtcars.wt<2200)]
print(mtcars_4cyl['mpg'].mean())
#5
n_man=mtcars['am'].sum()
print(n_man)

n_automatic=mtcars[mtcars.am==0]
print(len(n_automatic))
#6
mtcars_z6=mtcars[(mtcars.am==0) & (mtcars.hp>100)]
print(len(mtcars_z6))

#7

mtcars['kg']=mtcars.wt*453
print(mtcars.kg)