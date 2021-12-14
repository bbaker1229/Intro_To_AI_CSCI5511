#!/usr/bin/python3

""""
Bryan Baker
bake1358@umn.edu
CSCI 5511 - Final Exam
Question 2: Propositional Logic Satisfiability
"""

import string
import random
import sat_interface

def rand3cnf(m, n):
    symbols = list(string.ascii_uppercase)[:n]
    clauses = list()
    while len(clauses) < m:
        syms2use = random.sample(symbols, 3)
        clause = ""
        for sym in syms2use:
            preval = random.choice(["", "~"])
            clause += preval + sym + " "
            if clause not in clauses:
                clauses.append(clause)
    return clauses

rand3cnf(4, 5)
