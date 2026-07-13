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
        return 0
    
    return 1

assert bracket_matcher("(hello (world))") == 1, "Failed basic nested matching"
assert bracket_matcher("((hello (world))") == 0, "Failed unmatched opening bracket"
assert bracket_matcher("(coder)(byte))") == 0, "Failed example case 1"
assert bracket_matcher("(c(oder)) b(yte)") == 1, "Failed example case 2"
assert bracket_matcher("hello world") == 1, "Failed string with no brackets"
assert bracket_matcher("") == 1, "Failed empty string"
assert bracket_matcher(")(") == 0, "Failed order trap: closing bracket before opening"
assert bracket_matcher("(a)(b))(") == 0, "Failed complex order trap"
assert bracket_matcher("(((a))) b (c)") == 1, "Failed deeply nested valid brackets"
assert bracket_matcher("(((a)) b (c)") == 0, "Failed deeply nested invalid brackets"

print("All tests passed successfully!")