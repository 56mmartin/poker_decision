import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# bet/bluff grid
coarseness = 0.1
bet = np.arange(0, 10, 0.25 * coarseness)  # we assume a pot size of 1
bluff = np.arange(0, 1, 0.001 * coarseness)
bet, bluff = np.meshgrid(bet, bluff)

# P2's decisions
EV_P2_folds_when_P1_bets = 0
EV_P2_calls_when_P1_bets = (bluff + (bluff - 1) * bet) / (1 + bluff)

# P1's decisions
Prob_P1_bets = 1/2 + 1/2 * bluff  # always bets with good hands, sometimes bluffs with bad hands
EV_P1_if_P1_doesnt_bet = 0  # no bet => bad hand => always loses
EV_P1_if_P1_bets_and_P2_folds = 1  # P1 always wins except when she doesn't bluff
EV_P1_if_P1_bets_and_P2_calls = (1 + bet - bluff * bet) / (1 + bluff)
EV_P1_if_P1_bets = np.where(EV_P2_calls_when_P1_bets > EV_P2_folds_when_P1_bets,
                            EV_P1_if_P1_bets_and_P2_calls, EV_P1_if_P1_bets_and_P2_folds)
EV_P1 = Prob_P1_bets * EV_P1_if_P1_bets + (1 - Prob_P1_bets) * EV_P1_if_P1_doesnt_bet

# Plot the surface.
surf = ax.plot_surface(bet, bluff, EV_P1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_zlim(0, 1)
ax.set_xlabel("Bet size")
ax.set_ylabel("Bluff %")
ax.set_zlabel("EV")
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
