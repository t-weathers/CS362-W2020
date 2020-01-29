# -*- coding: utf-8 -*-
"""
Created on Thur Jan 14

@author: weathert
"""

import Dominion
import testUtility
import random
from collections import defaultdict

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

# number of curses and victory cards
if len(player_names) > 2:
    nV = 12
else:
    nV = 8
nC = -10 + 10 * len(player_names)

# generate the box of cards
box = testUtility.getBox(nV)

supply_order = testUtility.getOrder()

# pick 10 cards from box to be in supply
supply = testUtility.pick10(box)

# add default cards to supply
testUtility.addDefaultSupplyCards(supply, nV, nC, player_names)

# initialize the trash
trash = []

# Costruct the Player objects
players = []
testUtility.createPlayers(players,player_names)

###############################
# BUG
# (repeated call will assign 2x the player in the game.
###############################
testUtility.createPlayers(players,player_names)

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)