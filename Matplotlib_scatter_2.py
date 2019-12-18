from matplotlib import pyplot as plt
import numpy as np
# Generating a Gaussion dTset:
#Creating random vectors from the multivaritate normal distribution
#givem mean and covariance

mu_vecl = np.array([0, 0])
cov_matl = np.array([[2,0],[0,2]])

x1_samples = np.random.multivariate_normal(mu_vecl, cov_matl,100)
x2_samples = np.random.multivariate_normal(mu_vecl+0.2, cov_matl +0.2, 100)
x3_samples = np.random.multivariate_normal(mu_vecl+0.4, cov_matl +0.4, 100)

plt.figure(figsize = (8, 6))

plt.scatter(x1_samples[:,0], x1_samples[:, 1], marker='x',
           color = 'blue', alpha=0.7, label = 'x1 samples')
plt.scatter(x2_samples[:,0], x1_samples[:,1], marker='o',
           color ='green', alpha=0.7, label = 'x2 samples')
plt.scatter(x3_samples[:,0], x1_samples[:,1], marker='^',
           color ='red', alpha=0.7, label = 'x3 samples')
plt.title('Basic scatter plot')
plt.ylabel('variable X')
plt.xlabel('Variable Y')
plt.legend(loc = 'upper right')

plt.show()


import matplotlib.pyplot as plt

fig,ax = plt.subplots()

ax.plot([0],[0], marker="o",  markersize=10)
ax.plot([0.07,0.93],[0,0],    linewidth=10)
ax.scatter([1],[0],           s=100)

ax.plot([0],[1], marker="o",  markersize=22)
ax.plot([0.14,0.86],[1,1],    linewidth=22)
ax.scatter([1],[1],           s=22**2)

plt.show()


import matplotlib.pyplot as plt

for dpi in [72,100,144]:

    fig,ax = plt.subplots(figsize=(1.5,2), dpi=dpi)
    ax.set_title("fig.dpi={}".format(dpi))

    ax.set_ylim(-3,3)
    ax.set_xlim(-2,2)

    ax.scatter([0],[1], s=10**2, 
               marker="s", linewidth=0, label="100 points^2")
    ax.scatter([1],[1], s=(10*72./fig.dpi)**2, 
               marker="s", linewidth=0, label="100 pixels^2")

    ax.legend(loc=8,framealpha=1, fontsize=8)

    fig.savefig("fig{}.png".format(dpi), bbox_inches="tight")

plt.show() 