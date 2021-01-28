import random 

from modules.entities import *
from modules.inventory import *
from modules.items import *

class Commandplayer():
    def __init__(self, terminal):
        self.terminal = terminal

        self.player = Player("Momin", 20, 5)
        self.blob = Enemy("blob", 15, 3, random.randint(2, 4))

    def terminalOutput(self, result):
        if result == "stats":
            self.terminal.insert(1, str(self.player.helloPlayer()))
            self.terminal.pack()

        if result == "attack":
            self.terminal.insert(2, str(self.player.attack_enemy(self.blob)))
            self.terminal.pack()