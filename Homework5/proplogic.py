#!/usr/bin/python3

""""
Bryan Baker
bake1358@umn.edu
CSCI 5511 - Homework 5
Propositional Logic: Basic Logic
"""

import sat_interface


def example_problem():
    print("Liars and Truth-tellers Example Problem:")
    example_prob = sat_interface.KB(["~A ~B", "B A", "~B ~C", "C B", "~C ~A", "~C ~B", "A B C"])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    if example_prob.test_literal("A") and not example_prob.test_literal("~A"):
        print("Amy is a truth-teller.")
    elif example_prob.test_literal("~A") and not example_prob.test_literal("A"):
        print("Amy is a liar.")
    else:
        print("Not enough information about Amy to decide.")
    if example_prob.test_literal("B") and not example_prob.test_literal("~B"):
        print("Bob is a truth-teller.")
    elif example_prob.test_literal("~B") and not example_prob.test_literal("B"):
        print("Bob is a liar.")
    else:
        print("Not enough information about Bob to decide.")
    if example_prob.test_literal("C") and not example_prob.test_literal("~C"):
        print("Cal is a truth-teller.")
    elif example_prob.test_literal("~C") and not example_prob.test_literal("C"):
        print("Cal is a liar.")
    else:
        print("Not enough information about Cal to decide.")
    print("")


def tt2():
    print("Liars and Truth-tellers II:")
    example_prob = sat_interface.KB(["~A A", "~A C", "~A A ~C", "~B ~C", "C B", "~C B ~A", "~B C", "A C"])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    if example_prob.test_literal("A") and not example_prob.test_literal("~A"):
        print("Amy is a truth-teller.")
    elif example_prob.test_literal("~A") and not example_prob.test_literal("A"):
        print("Amy is a liar.")
    else:
        print("Not enough information about Amy to decide.")
    if example_prob.test_literal("B") and not example_prob.test_literal("~B"):
        print("Bob is a truth-teller.")
    elif example_prob.test_literal("~B") and not example_prob.test_literal("B"):
        print("Bob is a liar.")
    else:
        print("Not enough information about Bob to decide.")
    if example_prob.test_literal("C") and not example_prob.test_literal("~C"):
        print("Cal is a truth-teller.")
    elif example_prob.test_literal("~C") and not example_prob.test_literal("C"):
        print("Cal is a liar.")
    else:
        print("Not enough information about Cal to decide.")
    print("")


def tt3():
    print("Liars and Truth-tellers III:")
    example_prob = sat_interface.KB(["~A ~C", "C A", "~B A", "~B C", "~A ~C B", "~C B", "~B C"])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    if example_prob.test_literal("A") and not example_prob.test_literal("~A"):
        print("Amy is a truth-teller.")
    elif example_prob.test_literal("~A") and not example_prob.test_literal("A"):
        print("Amy is a liar.")
    else:
        print("Not enough information about Amy to decide.")
    if example_prob.test_literal("B") and not example_prob.test_literal("~B"):
        print("Bob is a truth-teller.")
    elif example_prob.test_literal("~B") and not example_prob.test_literal("B"):
        print("Bob is a liar.")
    else:
        print("Not enough information about Bob to decide.")
    if example_prob.test_literal("C") and not example_prob.test_literal("~C"):
        print("Cal is a truth-teller.")
    elif example_prob.test_literal("~C") and not example_prob.test_literal("C"):
        print("Cal is a liar.")
    else:
        print("Not enough information about Cal to decide.")
    print("")


def salt():
    print("Robbery and a Salt:")
    example_prob = sat_interface.KB(["~A ~B ~C", "A B C"])
    if example_prob.is_satisfiable():
        print("The knowledge base is satisfiable.")
    else:
        print("The knowledge base is not satisfiable.  Try again.")
        return None
    example_prob = sat_interface.KB(["~A ~B ~C", "A B C", "~B", "~C", "~A"])
    print(example_prob.is_satisfiable())
    """
    if example_prob.test_literal("A") and not example_prob.test_literal("~A"):
        print("Caterpillar ate the salt.")
    elif example_prob.test_literal("~A") and not example_prob.test_literal("A"):
        print("Caterpillar did not eat the salt.")
    else:
        print("Not enough information about Caterpillar to decide.")
    if example_prob.test_literal("B") and not example_prob.test_literal("~B"):
        print("Bill the Lizard ate the salt.")
    elif example_prob.test_literal("~B") and not example_prob.test_literal("B"):
        print("Bill the Lizard did not eat the salt.")
    else:
        print("Not enough information about Bill the Lizard to decide.")
    if example_prob.test_literal("C") and not example_prob.test_literal("~C"):
        print("Cheshire Cat ate the salt.")
    elif example_prob.test_literal("~C") and not example_prob.test_literal("C"):
        print("Cheshire Cat ate the salt.")
    else:
        print("Not enough information about Cheshire Cat to decide.")
    """
    print("")


def main():
    example_problem()
    tt2()
    tt3()
    salt()


if __name__ == "__main__":
    main()
