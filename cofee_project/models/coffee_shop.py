from typing import List
from menu import Menu
from staff import Staff
from table import Table


class CoffeeShop:
    def __init__(self, menus: List[Menu] = None, staffs: List[Staff] = None, tables: List[Table] = None):
        self.menus = menus
        self.staffs = staffs
        self.tables = tables

    def GetTable(self):
        return self.tables

    def GetStaffs(self):
        return self.staffs

    def GetMenus(self):
        return self.menus
