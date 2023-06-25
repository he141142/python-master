from typing import Dict


class IMenuItem:
    def GetName(self):
        pass

    def GetCost(self):
        pass

    def GetIngredients(self):
        pass

    def WithName(self, name: str):
        pass

    def WithCost(self, cost: float):
        pass

    def WithIngredients(self, ingredients: Dict):
        pass


class MenuItem(IMenuItem):
    def __init__(self, name=None, cost=None, ingredients=None):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

    def GetName(self):
        return self.name

    def GetCost(self):
        return self.cost

    def GetIngredients(self):
        return self.ingredients

    def WithCost(self, cost: float):
        self.cost = cost
        return self

    def WithName(self, name: str):
        self.name = name
        return self

    def WithIngredients(self, ingredients: Dict):
        self.ingredients = ingredients
        return self
