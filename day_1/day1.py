from turtle import Turtle
from prettytable import prettytable



def Exec():
    p = prettytable.PrettyTable()
    p.add_column("To do list", ["Learn AWS", "Learn English", "Learn NPL"])
    p.add_column("Target", ["pass", "7.0", "master certificated"])
    return p

