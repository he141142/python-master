from typing import List

from cofee_project.models.menu_item import IMenuItem


class Menu:
    def __init__(self):
        self.item: List[IMenuItem] = []
        self.type: str = ""

    def WithItem(self, items: List[IMenuItem]):
        self.item = items
        return self

    def AddItem(self, items: IMenuItem):
        self.item.append(items)
        return self

    def WithType(self, Type: str):
        self.type = Type
        return self

    def PrintAllItem(self):
        for idx, item in enumerate(self.item):
            print(f"item name: {item.GetName()} item cost: {item.GetCost()}")
