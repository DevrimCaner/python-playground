def bracket_combinations(num):
    if num <= 1:
        return 1
    
    mid_length = (num * 2) - 2
    pool = []
    valid_count = 0
    
    def backtrack(current):
        if len(current) == mid_length:
            pool.append(current)
            return
        # Start Recursive Loop
        backtrack(current + '(')
        backtrack(current + ')')
    
    # Create the combination pool
    backtrack('')
    # Check validation of every combination
    for text in pool:
        if bracket_matcher(f"({text})"):
            valid_count += 1
    
    return valid_count

# Helper Function
def bracket_matcher(text):
    counter = 0
    
    for char in text:
        if char == '(':
            counter += 1
        if char == ')':
            counter -=1
        
        if counter < 0:
            break
    
    if counter != 0:
        return False
    
    return True


assert bracket_combinations(1) == 1, "Failed for num = 1 (Expected 1: '()')"
assert bracket_combinations(2) == 2, "Failed for num = 2 (Expected 2: '()()', '(())')"
assert bracket_combinations(3) == 5, "Failed for num = 3 (Expected 5)"
assert bracket_combinations(4) == 14, "Failed for num = 4 (Expected 14)"
assert bracket_combinations(5) == 42, "Failed for num = 5 (Expected 42)"
assert bracket_combinations(6) == 132, "Failed for num = 6 (Expected 132)"
assert bracket_combinations(10) == 16796, "Failed for num = 10 (Expected 16796)"
assert bracket_combinations(0) == 1, "Failed for num = 0 (Expected 1: the empty set)"

print("All tests passed successfully!")