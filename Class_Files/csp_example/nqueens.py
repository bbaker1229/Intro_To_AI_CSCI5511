'''
N Queens puzzle solved in various ways
'''
import sys


def nqueens(n):
    '''constraints will be hard-coded: no queen can attack another queen'''
    varnames = []
    domains = {}
    for i in range(n):
        varnames.append('Q' + str(i))
        domains[varnames[i]] = list(range(n))
    res = backtrack_search(varnames, domains)
    if res == None:
        return False
    listresult = []
    for var in res:
        listresult.append((int(var[1:]), res[var]))
    listresult.sort()
    return listresult

def backtrack_search(variables, domains):
    return backtrack({}, variables, domains)

def backtrack(assignment, variables, domains):
    #print(len(assignment))
    if len(assignment) == len(variables):
        return assignment
    var = select_unassigned_variable(assignment, variables, domains)
    ordered_domain = order_domain(assignment, variables, domains, var)
    for val in domains[var]:
        assignment[var] = val
        inference_result = infer(var, assignment, variables, domains)
        if test_inference(domains):
            result = backtrack(assignment, variables, domains)
            if result != None:
                return result
        
        undo_inference(inference_result, domains)
        del assignment[var]
    return None

def order_domain(assignment, variables, domains, var):
    '''
    Order the domain variables such that least constraining come first
    assignment: the current assignment
    variables: the variable name list
    domains: the map from var names to domains
    var: the variable whose domain we are ordering
    '''
    return domains[var]
    ordered_tups = []
    for val in domains[var]:
        assignment[var] = val
        inf_count = infer_count(var, assignment, variables, domains)
        del assignment[var]
        ordered_tups.append((inf_count, val))
    ordered_tups.sort()
    ordered_tups.reverse()
    ordered_dom_vals = []
    for tup in ordered_tups:
        ordered_dom_vals.append(tup[1])
    return ordered_dom_vals

def test_inference(domains):
    for var in domains:
        if len(domains[var]) == 0:
            return False
    return True

def infer_count(var, assignment, variables, domains):
    '''
    we have just added an assignment for var and we're going to count how many 
    values would be eliminated if we went with it    
    '''
    qpos = (int(var[1:]), assignment[var])
    removed = {}
    for var2 in variables:
        if var2 not in assignment:
            removed[var2] = []
            for value in domains[var2]:
                q2pos = (int(var2[1:]), value)
                if attack(qpos, q2pos):
                    removed[var2].append(value)
    count = 0
    for var2 in removed:
        for val in removed[var2]:
            count += len(removed[var2])
    return count

def infer(var, assignment, variables, domains):
    '''we have just added an assignment for var and need to process its implications'''
    qpos = (int(var[1:]), assignment[var])
    removed = {}
    for var2 in variables:
        if var2 not in assignment:
            removed[var2] = []
            for value in domains[var2]:
                q2pos = (int(var2[1:]), value)
                if attack(qpos, q2pos):
                    removed[var2].append(value)
    for var2 in removed:
        for val in removed[var2]:
            domains[var2].remove(val)
    return removed

def find_not_attack(pos1, var2, domain2):
    xpos2 = int(var2[1:])
    for ypos2 in domain2:
        if not attack(pos1, (xpos2, ypos2)):
            return True
    return False

def revise(assignment, variables, domains, xi, xj, removed):
    revised = False
    ipos = int(xi[1:])
    to_remove = []
    for vali in domains[xi]:
        if not find_not_attack((ipos, vali), xj, domains[xj]):
            removed[xi].append(vali)
            revised = True
    for v in removed[xi]:
        domains[xi].remove(v)
    return revised

def ac3(var, assignment, variables, domains):
    '''
    Do inference with AC3
    '''
    queue = []
    removed = {}
    for xi in variables:
        removed[xi] = []
        for xj in variables:
            if xi != xj:
                queue.append((xi, xj))
    while len(queue) != 0:
        arc = queue.pop(0)
        if revise(assignment, variables, domains, xi, xj, removed):
            if len(domains[xi]) == 0:
                #undo removals
                return {}
            for xk in variables:
                if xk != xj and xk != xi:
                    queue.append((xi, xk))
    return removed

def undo_inference(removed, domains):
    for var2 in removed:
        for val in removed[var2]:
            domains[var2].append(val)

def select_unassigned_variable(assignment, variables, domains):
    mindom = 100000
    var = None
    for i in variables:
        if i not in assignment and len(domains[i]) < mindom:
            mindom = len(domains[i])
            var = i
    return var
'''
def select_unassigned_variable(assignment, variables, domains):
    for i in variables:
        if i not in assignment:
            return i
    return None
'''
def attack(pos1, pos2):
    '''
    return true if a queen at pos1 can attack pos2 on an nxn board

    pos1 a tuple (x1,y1)

    pos2 a tuple (x2,y2)
    '''
    return (pos1[0] == pos2[0] or pos1[1] == pos2[1] or 
           abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1]))


def main():
    print(nqueens(int(sys.argv[1])))

main()
