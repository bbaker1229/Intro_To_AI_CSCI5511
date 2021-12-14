#!/usr/bin/python3

""""
Bryan Baker
bake1358@umn.edu
CSCI 5511 - Final Exam
Question 2: Propositional Logic Satisfiability
"""

import string
import random
import numpy as np
import sat_interface


# Part a.) Write the rand3cnf function.
def rand3cnf(m, n):
    """
    This function returns a random propositional logic sentence in the 3-CNF form using m clauses and n symbols.
    :param m: The number of clauses to create as an integer.
    :param n: The number of symbols to generate from as an integer.
    :return: A list of clauses to be used for a knowledge base.
    """
    symbols = list(string.ascii_uppercase)[:n]  # Create the list of possible symbols to use.
    clauses = list()
    while len(clauses) < m:  # Continue generating clauses to add until the number of items reaches m
        syms2use = random.sample(symbols, 3)  # Get the 3 symbols to use for this clause
        clause = ""
        for sym in syms2use:
            preval = random.choice(["", "~"])  # Each symbol may or may not become negated
            clause += preval + sym + " "  # Create the clause
        if clause not in clauses:
            clauses.append(clause)  # Add the clause to the list of clauses as long as it is a new clause.
    return clauses


# Part b.) Write a function that will call the function from part a...
def createkbs():
    """
    This function prints out the m and n values and calls the rand3cnf function 100 times to calculate a percentage
    that the created knowledge base is satisfiable. The results are the printed out.
    """
    print(" m  n percent_satisfiable")
    print("-- -- -------------------")
    for m in [30, 40, 50, 60, 70]:
        for n in [10, 15, 20]:
            cnt = 0
            for i in range(100):
                clauses = rand3cnf(m, n)
                KB = sat_interface.KB(clauses)
                if KB.is_satisfiable():
                    cnt += 1
            print(m, n, round(cnt/100, 1))


def createstats():
    """
    This function was used for testing to run each m and n value 100 times as in createkbs and then the mean and
    sigma was calculated for each to determine which items were more "interesting".
    """
    print(" m  n   mean  sigma")
    print("-- -- ------ ------")
    for m in [30, 40, 50, 60, 70]:
        for n in [10, 15, 20]:
            runs = list()
            for j in range(100):
                cnt = 0
                for i in range(100):
                    clauses = rand3cnf(m, n)
                    KB = sat_interface.KB(clauses)
                    if KB.is_satisfiable():
                        cnt += 1
                runs.append(cnt/100)
            print(m, n, round(np.mean(runs), 4), round(np.std(runs), 4))


createkbs()
# createstats()
"""
Part c.)
The createstats function suggests that the following m, n pairs are interesting (not 0 or 1):
 m   n
--  -- 
40, 10
50, 10
60, 10
60, 15
70, 15
The other values were either 1 or very close to 0.  The createstats function gives a better picture of 
which items are more interesting since more runs are created.  It looks like the range for interesting KBs 
is around n/m < 0.3.  Anything greater than 0.3 and the percentage of satisfiable KBs approaches 1.  
"""
