class Merchant:
    def __init__ (self, name,products):
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(self.products)
Joanna = Merchant("Joanna", ['alfreds', 'pork'])
Joanna.sell('pork')
Alvin = Merchant("Alvin", ["Human", "Alvin's Servitude", "Organs"])
Alvin.sell("Human")