

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

class Weapon:

    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability

    def getName(self):
        return self.name

    def get_damage(self):
        return self.damage
