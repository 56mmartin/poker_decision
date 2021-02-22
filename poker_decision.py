import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
bet = np.arange(0, 5, 0.25)
bluff = np.arange(0, 1, 0.1)
bet, bluff = np.meshgrid(bet, bluff)
EV_P2 = np.sqrt(bet**2 + bluff**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(bet, bluff, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()