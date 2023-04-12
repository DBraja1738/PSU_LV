import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars= pd.read_csv('mtcars.csv')
#1
mtcars_4cyl=mtcars[mtcars.cyl==4]
mtcars_6cyl=mtcars[mtcars.cyl==6]
mtcars_8cyl=mtcars[mtcars.cyl==8]

mtcars_4cylmean=mtcars_4cyl['mpg'].mean()
mtcars_6cylmean=mtcars_6cyl['mpg'].mean()
mtcars_8cylmean=mtcars_8cyl['mpg'].mean()
mpg=[mtcars_4cylmean,mtcars_6cylmean,mtcars_8cylmean]
cyl=[4,6,8]

#plt.bar(cyl,mpg)
#plt.show()

#2

#mtcars.boxplot(column='wt',by='cyl')
#plt.show()

#3
mtcars_auto=mtcars[mtcars.am==0]
mtcars_man=mtcars[mtcars.am==1]

auto_mpg=mtcars_auto['mpg'].mean()
man_mpg=mtcars_man['mpg'].mean()


#plt.bar(["automatic","manual"],[auto_mpg,man_mpg])
#plt.show()



plt.scatter(mtcars_auto['hp'], mtcars_auto['qsec'], color='black', label='automatic')
plt.scatter(mtcars_man['hp'], mtcars_man['qsec'], color='red', label='manual')
plt.legend()
plt.show()