import os
import random
import time
from tkinter import *

from modules.entities import *
from modules.inventory import *
from modules.items import *


# setup
def clear(): 
     return os.system('cls')

# inventory
money = Wallet(100)

# weapons
knife = Weapon("Knife", 2, 10)
sword = Weapon("Sword", 4, 15)

# players
player = Player("Momin", 20, knife.get_damage())

# enemies
blob = Enemy("blob", 10, 1, random.randint(3, 10))

# main game
while True:
    # attacks
    blob.attack_player(player)
    player.attack_enemy(blob)
    # Dead
    if player.health <= 0:
        player.dead()
        break

    if blob.health <= 0:
        blob.dead()
        money.addCoin(blob.lootCoin())

    time.sleep(3)
    clear()
    print("Player info")
    print("|", player.getPseudo(), "|", player.getHealth(),
          "❤️ |", money.getCoinAmount(), "💸 |")
    print("|", knife.getName(), " |", player.getAttack())
    print("|     |     |     |")
    time.sleep(1)

clear()