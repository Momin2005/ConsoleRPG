from tkinter import *

class Player:
    
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack

    def helloPlayer(self):
        return self.pseudo, "/ health:", self.health, "/ attack:", self.attack

    def getPseudo(self):
        return self.pseudo

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_enemy(self, target_enemy):
        target_enemy.damage(self.attack)
        return "You attacked", target_enemy.name, ", he lost", self.attack, "HP. His current health is", target_enemy.health

    def dead(self):
        if self.health <= 0:
            print(self.pseudo, "is dead")


class Enemy:
    
    def __init__(self, name, health, attack, coins):
        self.name = name
        self.health = health
        self.attack = attack
        self.coins = coins

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage
        
    def lootCoin(self):
        return self.coins

    def attack_player(self, target_player):
        target_player.damage(self.attack)
        return "You attacked", target_player.name, ", he lost", self.attack, "HP. His current health is", target_player.health

    def dead(self):
        print(self.name, "is dead")