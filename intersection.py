def find_intersection(strArr):
    set1 = {x.strip() for x in strArr[0].split(',')}
    set2 = {x.strip() for x in strArr[1].split(',')}

    # Find the intersection using the '&' operator\
    intersection = sorted(list(set1 & set2), key=int)
    return ",".join(intersection)

assert find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]) == "1,4,13"
assert find_intersection(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]) == "1,9,10"