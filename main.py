from sympy import *
from sympy.logic.boolalg import to_cnf, Not, And, Or


def belief_base():
    # Initialize empty beliefs in an array
    beliefs = []

    # Infinite loop to keep prompting the user to insert new beliefs to make belief revision.
    while True:
        # Prompt the user to enter a belief
        belief_str = input("Enter a belief (or 'done' to finish): ")

        # If the user types "done" in console the program will stop running
        if belief_str == "done":
            break

        # Parse the belief expression into a sympy expression
        belief = sympify(belief_str)

        # Checking for contradictions in the belief base and swap the conflicting beliefs with the new belief
        conflicting_beliefs = []
        for c in beliefs:
            if simplify(belief & c) == false:
                conflicting_beliefs.append(c)
        if conflicting_beliefs:
            print("Contradiction found. The new belief contradicts the following beliefbase:", conflicting_beliefs)
            beliefs = [c if c not in conflicting_beliefs else belief for c in beliefs]
            continue

        # This condition will check if there are any duplicate beliefs in the belief base
        if belief in beliefs:
            print("Duplicate found. Please try again.")
            continue

        # Add the belief to the list of beliefs
        beliefs.append(belief)

        # Print newest belief
        print("Current beliefs:", beliefs)

    # Print the final CNF in belief form
    cnf = simplify(And(*beliefs))
    beliefs = list(cnf.args)
    print("The final CNF for belief base:", beliefs)


if __name__ == "__main__":
    belief_base()
