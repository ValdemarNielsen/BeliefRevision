from typing import List
from sympy import *

x, y = symbols('x,y')


def check_logic(var, value):
    # assume var is always true for now
    return True


def belief_base():
    print("hello")


def check_syntax(var):
    logic = ["&", "~", "|", "->", "<->", "(", ")"]


def knowledge_base() -> List:
    knowledgeBase = []
    var = input("Enter a variable: ")
    value = input("Enter a value: ")
    knowledgeBase.append(var)
    knowledgeBase.append(value)

    if check_logic(var, value):
        print("The variable is true")

    return knowledgeBase


def run():
    while true:
        knowledge_base()


run()
