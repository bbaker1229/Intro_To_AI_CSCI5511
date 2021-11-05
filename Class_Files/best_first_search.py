# more python-esque pseudocode for best-first-search
# not using generator structure
# from page 73
def best_first_search(init_state):

    node = Node(init_state)
    frontier = empty list/queue/stack/etc
    frontier.add(node)
    reached = {}
    reached[init_state] = node

    while not frontier.is_empty():
        node = frontier.remove()

        if node.state == goal: return node

        for child in get_children(node):

            s = child.state

            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.add(child)
    return failure

def get_children(node):
    children = []
    s = node.state
    for each action in Actions(s):
        sp = Result(s, action)
        cost = node.path_cost + Path_Cost(s, action, sp)
        children.add(Node(sp, action, cost))
    return children
