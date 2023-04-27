from sympy import *
from itertools import combinations
from sympy.logic.boolalg import to_cnf, Not, And, Or


def belief_Revision():

    beliefBase = []

    while True:

        logic_Input = input("Enter a belief (or 'done' to finish): ")

        if logic_Input == "done":
            break

        # Translate the input into a sympy expression
        belief = sympify(logic_Input)

        # Contradiction-check in the belief base
        conflict_combination = []
        for i in range(1, len(beliefBase) + 1):
            for c in combinations(beliefBase, i):
                if simplify(belief & And(*c)) == false:
                    conflict_combination.append(c)

        # Deletion of conflicting combinations
        for c in conflict_combination:
            if set(c).issubset(set(beliefBase)):
                beliefBase = [b for b in beliefBase if b not in c]
                print(f"Removing beliefs {c} due to contradiction with {belief}")

        # Duplicate check
        if belief in beliefBase:
            print("Duplicate found. Please try again.")
            continue

        beliefBase.append(belief)

        print("Current beliefs:", beliefBase)

    cnf = simplify(And(*beliefBase))
    beliefBase = list(cnf.args)
    print("The final CNF for belief base:", beliefBase)


if __name__ == "__main__":
    belief_Revision()
