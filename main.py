# This is a sample Python script.
from day_1 import *
from cofee_project.models.staff import Staff
from cofee_project.models.menu_item import MenuItem
from cofee_project.models.menu import Menu


def add(x, y):
    return x + y


def Exec_():
    day_1_partial.runDay1()
    print(Exec())
    return 1, "@fpt"


print(add(2, 3))
num, str = Exec_()
print(num, str)

# st = Staff("Role", 12, 121, "222")
# # menuItem = MenuItem("Coffee", 12, {
# #     "in": 12,
# # })
# # st.Order(menuItem, 2)

menu = Menu().WithType("Food") \
    .AddItem(MenuItem()
             .WithName("Coffee")
             .WithCost(12.9)
             ) \
    .AddItem(MenuItem()
             .WithName("Matcha")
             .WithCost(13.00))

menu.PrintAllItem()
