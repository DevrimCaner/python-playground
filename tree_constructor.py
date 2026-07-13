import ast
def tree_constructor(strArr):
    parent_of ={}
    child_count ={}
    root_candidates = set()

    for s in strArr:
        # Convert into touple
        t = ast.literal_eval(s)

        # Check double parenting
        if parent_of.get(t[0], 0) :
            return False
        parent_of[t[0]] = t[1]

        # Check child count
        child_count[t[1]] = child_count.get(t[1], 0) + 1
        if child_count[t[1]] > 2:
            return False

        # Manage root candidates
        if t[1] not in parent_of:
            root_candidates.add(t[1])
        root_candidates.discard(t[0])

    if len(root_candidates) != 1:
        return False

    # Finally every thing is okey  
    return True

def tree_constructor_better(str_arr: list[str]) -> bool:
    parent_of = {}
    child_count = {}
    
    for s in str_arr:
        child, parent = s.strip("()").split(",")

        if child in parent_of:
            return False
        parent_of[child] = parent
        

        child_count[parent] = child_count.get(parent, 0) + 1
        if child_count[parent] > 2:
            return False
    
    roots = {p for p in child_count if p not in parent_of}
    
    return len(roots) == 1

assert tree_constructor(["(1,2)", "(2,4)", "(7,2)"]) == True
assert tree_constructor(["(2,1)", "(3,1)"]) == True
assert tree_constructor(["(5,10)"]) == True
assert tree_constructor(["(1,2)", "(1,3)"]) == False
assert tree_constructor(["(2,1)", "(3,1)", "(4,1)"]) == False
assert tree_constructor(["(1,2)", "(3,4)"]) == False
assert tree_constructor(["(2,1)","(3,1)","(4,2)","(5,2)","(6,3)","(7,3)"]) == True
assert tree_constructor(["(2,1)","(3,1)","(4,2)"]) == True
assert tree_constructor(["(4,2)", "(5,2)", "(2,1)", "(3,1)"]) == True
assert tree_constructor(["(2,1)", "(4,3)", "(3,1)"]) == True

assert tree_constructor_better(["(1,2)", "(2,4)", "(7,2)"]) == True
assert tree_constructor_better(["(2,1)", "(3,1)"]) == True
assert tree_constructor_better(["(5,10)"]) == True
assert tree_constructor_better(["(1,2)", "(1,3)"]) == False
assert tree_constructor_better(["(2,1)", "(3,1)", "(4,1)"]) == False
assert tree_constructor_better(["(1,2)", "(3,4)"]) == False
assert tree_constructor_better(["(2,1)","(3,1)","(4,2)","(5,2)","(6,3)","(7,3)"]) == True
assert tree_constructor_better(["(2,1)","(3,1)","(4,2)"]) == True
assert tree_constructor_better(["(4,2)", "(5,2)", "(2,1)", "(3,1)"]) == True
assert tree_constructor_better(["(2,1)", "(4,3)", "(3,1)"]) == True

print("All tests passed!")