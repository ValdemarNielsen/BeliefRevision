from typing import List
from sympy import *

x, y = symbols('x,y')

class BeliefRevision():
    def init(self):
        self.knowledgeBase = []
        self.beliefBase = []

    def check_logic(self, var, value):
        # assume var is always true for now
        return True

    def belief_base(self):
        print("hello")

    def knowledge_base(self) -> List:
        knowledgeBase = []
        var = input("Enter a variable: ")
        value = input("Enter a value: ")
        knowledgeBase.append(var)
        knowledgeBase.append(value)

        if self.check_logic(var, value):
            print("The variable is true")

        return knowledgeBase

if __name__ == '__main__':
    BeliefRevision().knowledge_base()