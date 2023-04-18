from typing import List

from sympy import *
from sympy.logic import POSform

p, q, s, t = symbols('p, q, s, t')

def check_logic():
    print("hey")

def beliefBase():
    print("hello")

def knowledgeBase():
    print("howdy")

#Knowledge Base: P, Q, R and more
#Define P, Q, R and their values and "beliefs"
#Update the rest fo the knowledge base based on the new values and revision
#Start of by an empty knowledge base which is updated with the new values based on user input

def knowledgeBase() -> List:
    knowledgeBase = []
    knowledgeBase.append("P")
    knowledgeBase.append("Q")
    knowledgeBase.append("R")
    return knowledgeBase
