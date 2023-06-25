class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = []
