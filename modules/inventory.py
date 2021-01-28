
#money system
class Wallet:
    def __init__(self, coin):
      self.coin = coin
      
    def getCoinAmount(self):
      return self.coin
      
    def addCoin(self, amount):
      self.coin += amount
      print("You earned", amount,"coins")
      
    def removeCoin(self, amount):
      self.coin -= amount
      print("You losed", amount,"coins")

#item system
class item:
      def __init__(self, name, description):
        self.name = name
        self.description = description
        self.stack = 64 

      def getName(self):
        return self.name

      def getDescription(self):
            return self.description


      
      
