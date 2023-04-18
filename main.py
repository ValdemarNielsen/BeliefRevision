from typing import List

from sympy import *
x, y = symbols('x,y')

class BeliefRevision():
    def __init__(self, master=None):

        print("hello")



    def check_logic(self):
        print("hey")

    def beliefBase(self):
        print("hello")


#Knowledge Base: P, Q, R and more
#Define P, Q, R and their values and "beliefs"
#Update the rest fo the knowledge base based on the new values and revision
#Start of by an empty knowledge base which is updated with the new values based on user input

    def knowledgeBase(self) -> List:
        knowledgeBase = []
        knowledgeBase.append("P")
        knowledgeBase.append("Q")
        knowledgeBase.append("R")
        return knowledgeBase
