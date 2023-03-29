import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)
x=data[:,0]
y=data[:,3]
wt=data[:,5]
plt.scatter(x,y,marker=".",s=wt*150)

plt.ylabel("HP")
plt.xlabel("MPG")
for i in range(len(x)):
    plt.annotate(wt[i], (x[i], y[i] + 0.2))
print("min mpg:",np.min(x))
print("max mpg:",np.max(x))
print("avg mpg:",np.average(x))
idx=data[:,1]==6
data_=data[idx,:]
#print(idx)
#print(data_)
x_cyl=data_[:,0]
print("min",np.min(x_cyl))
print("max",np.max(x_cyl))
print("avg",np.mean(x_cyl))


plt.show()