import math

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

def bracket_combinations(num):
    """
    My First brute forcing solve
    """
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

def bracket_combinations_better(num: int) -> int:
    """
    This is a better solution than my brute force it's work O(N^2)
    """
    stack = []
    result = []

    def backtrack(open_count, close_count):
        # Means a pair founded
        if open_count == close_count == num:
            result.append("".join(stack))
            return
        # Can we add parentheses
        if open_count < num:
            stack.append('(')
            backtrack(open_count + 1, close_count)
            stack.pop()
        
        # Is available for closing
        if close_count < open_count:
            stack.append(')')
            backtrack(open_count, close_count + 1)
            stack.pop()
    
    backtrack(0, 0)
    return len(result)

def bracket_combinations_catalan(num: int) -> int:
    """
    This is the best way to solve this problem Best Way runs O(1)
    """
    if num < 0:
        return 0
    
    # Catalan Number Formula: comb(2n, n) // (n + 1)
    return math.comb(2 * num, num) // (num + 1)

assert bracket_combinations_catalan(0) == 1, "Failed for num = 0 (Expected 1: the empty set)"
assert bracket_combinations_catalan(1) == 1, "Failed for num = 1 (Expected 1: '()')"
assert bracket_combinations_catalan(2) == 2, "Failed for num = 2 (Expected 2)"
assert bracket_combinations_catalan(3) == 5, "Failed for num = 3 (Expected 5)"
assert bracket_combinations_catalan(4) == 14, "Failed for num = 4 (Expected 14)"
assert bracket_combinations_catalan(5) == 42, "Failed for num = 5 (Expected 42)"
assert bracket_combinations_catalan(6) == 132, "Failed for num = 6 (Expected 132)"
assert bracket_combinations_catalan(10) == 16796, "Failed for num = 10 (Expected 16796)"
assert bracket_combinations_catalan(15) == 9694845, "Failed for num = 15"

assert bracket_combinations_better(0) == 1, "Failed for num = 0 (Expected 1: the empty set)"
assert bracket_combinations_better(1) == 1, "Failed for num = 1 (Expected 1: '()')"
assert bracket_combinations_better(2) == 2, "Failed for num = 2 (Expected 2)"
assert bracket_combinations_better(3) == 5, "Failed for num = 3 (Expected 5)"
assert bracket_combinations_better(4) == 14, "Failed for num = 4 (Expected 14)"
assert bracket_combinations_better(5) == 42, "Failed for num = 5 (Expected 42)"
assert bracket_combinations_better(6) == 132, "Failed for num = 6 (Expected 132)"
assert bracket_combinations_better(10) == 16796, "Failed for num = 10 (Expected 16796)"
assert bracket_combinations_better(15) == 9694845, "Failed for num = 15"

assert bracket_combinations(0) == 1, "Failed for num = 0 (Expected 1: the empty set)"
assert bracket_combinations(1) == 1, "Failed for num = 1 (Expected 1: '()')"
assert bracket_combinations(2) == 2, "Failed for num = 2 (Expected 2: '()()', '(())')"
assert bracket_combinations(3) == 5, "Failed for num = 3 (Expected 5)"
assert bracket_combinations(4) == 14, "Failed for num = 4 (Expected 14)"
assert bracket_combinations(5) == 42, "Failed for num = 5 (Expected 42)"
assert bracket_combinations(6) == 132, "Failed for num = 6 (Expected 132)"
assert bracket_combinations(10) == 16796, "Failed for num = 10 (Expected 16796)"

print("All tests passed successfully!")