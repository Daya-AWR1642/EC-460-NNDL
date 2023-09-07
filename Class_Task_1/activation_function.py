import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

x = np.arange(-20,20)

# Plotting Sigmoid

y1 = 1/(1+np.exp(-x))
y2 = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
y3 = x / (1 + np.abs(x))
# Creating Subplot 
fig,axs = plt.subplots(2,2,figsize = (12,4))

# Plotting standard sigmoid on the first subplot 
axs[0][0].plot(x,y1)
axs[0][0].set_title('Sigmoid')
axs[0][0].set_xlabel('X axis')
axs[0][0].set_ylabel('Y axis')

# Plotting tanh function
axs[0][1].plot(x,y2)
axs[0][1].set_title('Tanh')
axs[0][1].set_xlabel('X axis')
axs[0][1].set_ylabel('Y axis')

axs[1][0].plot(x,y3)
axs[1][0].set_title('Softsign')
axs[1][0].set_xlabel('X axis')
axs[1][0].set_ylabel('Y axis')


plt.tight_layout()
plt.show()
