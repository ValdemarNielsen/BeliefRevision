from typing import List

from sympy import *
from sympy.logic import POSform

p, q, r, s, t = symbols('p, q, r, s, t')


def check_logic():
    print("hey")


def beliefBase():
    print("hello")


# Knowledge Base: p, q, r and more
# Define p, q, r and their values and "beliefs"
# Update the rest fo the knowledge base based on the new values and revision
# Start of by an empty knowledge base which is updated with the new values based on user input

def knowledgeBase() -> List:
    input1 = input()
    print(input1)
    knowledgeBase = []
    knowledgeBase.append("p")
    knowledgeBase.append("q")
    knowledgeBase.append("r")
    return knowledgeBase

def runitall():
    print("hello")

knowledgeBase()