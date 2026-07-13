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

assert tree_constructor(["(1,2)", "(2,4)", "(7,2)"]) == True
assert tree_constructor(["(2,1)", "(3,1)"]) == True
assert tree_constructor(["(5,10)"]) == True
assert tree_constructor(["(1,2)", "(1,3)"]) == False
assert tree_constructor(["(2,1)", "(3,1)", "(4,1)"]) == False
assert tree_constructor(["(1,2)", "(3,4)"]) == False
assert tree_constructor(["(2,1)","(3,1)","(4,2)","(5,2)","(6,3)","(7,3)"]) == True
assert tree_constructor(["(2,1)","(3,1)","(4,2)"]) == True

print("All tests passed!")