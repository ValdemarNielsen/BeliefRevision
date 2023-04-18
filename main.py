from typing import List

from sympy import *

x, y = symbols('x,y')

class BeliefRevision():
    def __init__(self):
        self.knowledgeBase = []
        self.beliefBase = []


    def check_logic(self):
        var = input("Enter a variable: ")
        value = input("Enter a value: ")
        print("hey")

    def beliefBase(self):
        print("hello")

#Knowledge Base: P, Q, R and more
#Define P, Q, R and their values and "beliefs"
#Update the rest fo the knowledge base based on the new values and revision
#Start of by an empty knowledge base which is updated with the new values based on user input
    def knowledgebase(self) -> List:
        knowledgeBase = []
        var = input("Enter a variable: ")
        value = input("Enter a value: ")
        knowledgeBase.append(var)
        knowledgeBase.append(value)

        if self.check_logic(self, var, value):
            print("The variable is true")

        return knowledgeBase

#Run the program
if __name__ == '__main__':
    BeliefRevision().knowledgebase()
