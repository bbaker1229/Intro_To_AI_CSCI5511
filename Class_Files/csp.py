#pseudocode for CSPs
def BACKTRACK(csp, assignment):
    if assignment is complete: return assignment
    var = Select_Unassigned_Varable(csp, assignment)
    for val in Order_Values(csp.domain[var]):
        if var = value is consistent:
            add {var = value} to assignment
            inferences = Inference(csp, var, assignment)
            if inferences != failure:
                add inferences to csp
                result = BACKTRACK(csp, assignment)
                if result != failure: return result
                remove inferences from csp
            remove {var = value} from assignment
    return failure


# AC3, one possible inference algorithm
def AC3(csp):
    queue = csp.get_arcs() # arcs = binary constraints
    while not queue.isempty():
        Xi, Xj = queue.pop()
        if Revise(csp):
            if len(csp.domain[i]) == 0: return False
            for Xk in Xi.neighbors():
                if Xk != Xj:
                    queue.add(Xk, Xi)
    return True

def Revise(csp, Xi, Xj):
    revised = False
    for x in csp.domain[i]:
        can_satisfy = False
        for y in csp.domain[j]:
            if (x,y) in csp.constraints[i][j]:
                can_satisfay = True
        if can_satisfy == False:
            csp.domain[i].remove(x)
            revised = True
    return revised
