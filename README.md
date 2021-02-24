poker_decision (Python3.6.9)

This is a very simplified poker-inspired two-player game with only one round and a pot size of 1. Only player 1 (P1, plays first) can bet (any size >= 0) and P2 can only fold or call.
P1 has either a good or bad hand, P2 always has an average hand. That means P1 knows whether she'll be winning on showdown or not, but P2 doesn't. However we assume they've been playing for a while so P2 knows P1's bluff percentage.
This code calculates the expected value of P1's bet (could be zero i.e. check) depending on the bet size and the bluff percentage. We assume P2 will maximise their expected value as well.

The conclusion is, it's best for P1 to adopt a very aggressive strategy whereby she overbets massively with nearly all of her hands, e.g. bet size = 10, bluff percentage = 95%. With that strategy P2 will always fold (because a slight majority of P1's hands are good) so P1 gets the pot nearly all the time (EV ~= 1), the only exception being when she's not bluffing.

Although this is a very simple model it gives credence to overbets as part of an aggressive poker strategy. 

