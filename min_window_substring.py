def min_window_substring(strArr):
    max_length = len(strArr[0])
    min_lenght = len(strArr[1])

    target_hash = {}
    for char in strArr[1]:
        target_hash[char] = target_hash.get(char, 0) + 1

    for current_length in range(min_lenght, max_length):
        for i in range(len(strArr[0]) - (current_length - 1)):
            current_substring = strArr[0][i:current_length + i]
            # Create a hash of current substring
            current_hash = {}
            for char in current_substring:
                current_hash[char] = current_hash.get(char, 0) + 1

            found_pair = True
            # Compare hashes
            for char, required_count in target_hash.items():
                available_count = current_hash.get(char, 0)
                
                if available_count < required_count:
                    found_pair = False
            # If it still thiks found a pair
            if found_pair == True:
                return current_substring
    # Return the full strin if no pairs
    return strArr[0]

def min_window_substring_better(strArr: list[str]) -> str:
    s = strArr[0]
    t = strArr[1]
    
    # 1. Map the target characters and their required counts
    target_hash = {}
    for char in t:
        target_hash[char] = target_hash.get(char, 0) + 1
        
    required_unique_chars = len(target_hash)
    
    # 2. Set up our sliding window tracking variables
    window_hash = {}
    formed = 0  # Tracks how many unique characters have met their target frequency
    
    # Track the smallest valid window: (length, substring)
    min_len = float("inf")
    min_window = ""
    
    left = 0
    
    # 3. Expand the window to the right
    for right in range(len(s)):
        char = s[right]
        window_hash[char] = window_hash.get(char, 0) + 1
        
        # If the current character count matches the target count, we formed a requirement
        if char in target_hash and window_hash[char] == target_hash[char]:
            formed += 1

        # 4. Once we have a valid window, shrink it from the left
        while left <= right and formed == required_unique_chars:
            current_window_len = right - left + 1
            
            # Save this window if it's the smallest we've seen so far
            if current_window_len < min_len:
                min_len = current_window_len
                min_window = s[left:right + 1]
                
            # Pop the left character out of the window
            left_char = s[left]
            window_hash[left_char] -= 1
            
            # If popping that character broke our valid window, update `formed`
            if left_char in target_hash and window_hash[left_char] < target_hash[left_char]:
                formed -= 1
                
            # Move the left pointer forward to shrink
            left += 1
    return min_window

assert min_window_substring(["aaabaaddae", "aed"]) == "dae"
assert min_window_substring(["aabdccdbcacd", "aad"]) == "aabd"
assert min_window_substring(["ahffaksfajeeubsne", "jefaa"]) == "aksfaje"
assert min_window_substring(["aaffhkksemckelloe", "fhea"]) == "affhkkse"
assert min_window_substring(["abc", "abc"]) == "abc"
assert min_window_substring(["abc", "a"]) == "a"
assert min_window_substring(["abc", "c"]) == "c"
assert min_window_substring(["aaab", "aa"]) == "aa"
assert min_window_substring(["baaac", "aaa"]) == "aaa"
assert min_window_substring(["abac", "aa"]) == "aba"
assert min_window_substring(["abcdxyz", "abc"]) == "abc"
assert min_window_substring(["xyzabcd", "bcd"]) == "bcd"
assert min_window_substring(["abc", "acb"]) == "abc"
assert min_window_substring(["a", "a"]) == "a"
assert min_window_substring(["cabefgecdaecf", "cae"]) == "aec"
assert min_window_substring(["bbaa", "aba"]) == "baa"

assert min_window_substring_better(["aaabaaddae", "aed"]) == "dae"
assert min_window_substring_better(["aabdccdbcacd", "aad"]) == "aabd"
assert min_window_substring_better(["ahffaksfajeeubsne", "jefaa"]) == "aksfaje"
assert min_window_substring_better(["aaffhkksemckelloe", "fhea"]) == "affhkkse"
assert min_window_substring_better(["abc", "abc"]) == "abc"
assert min_window_substring_better(["abc", "a"]) == "a"
assert min_window_substring_better(["abc", "c"]) == "c"
assert min_window_substring_better(["aaab", "aa"]) == "aa"
assert min_window_substring_better(["baaac", "aaa"]) == "aaa"
assert min_window_substring_better(["abac", "aa"]) == "aba"
assert min_window_substring_better(["abcdxyz", "abc"]) == "abc"
assert min_window_substring_better(["xyzabcd", "bcd"]) == "bcd"
assert min_window_substring_better(["abc", "acb"]) == "abc"
assert min_window_substring_better(["a", "a"]) == "a"
assert min_window_substring_better(["fcabefgecdaecf", "cae"]) == "aec"
assert min_window_substring_better(["bbaa", "aba"]) == "baa"

print("All tests passed!")