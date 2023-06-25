# This is a sample Python script.
from day_1 import *


def add(x, y):
    return x + y


def Exec_():
    day_1_partial.runDay1()
    print(Exec())
    return 1, "@fpt"


print(add(2, 3))
num, str = Exec_()
print(num, str)
