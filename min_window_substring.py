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

print("All tests passed!")