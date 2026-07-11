import re

def palindrome_check(text: str) -> bool:
    # Regular Expression
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text)
    reversed_text = cleaned[::-1]
    return cleaned.lower() == reversed_text.lower()

assert palindrome_check("") == True, "Error: Failed on empty string"
assert palindrome_check("a") == True, "Error: Failed on single character"
assert palindrome_check("   ") == True, "Error: Failed on string with only spaces"
assert palindrome_check("racecar") == True, "Error: Failed on a basic lowercase palindrome ('racecar')"
assert palindrome_check("hello") == False, "Error: Failed on a basic non-palindrome ('hello')"
assert palindrome_check("RaceCar") == True, "Error: Failed to ignore case ('RaceCar')"
assert palindrome_check("Level") == True, "Error: Failed to ignore case ('Level')"
assert palindrome_check("A man, a plan, a canal: Panama") == True, "Error: Failed on complex punctuation/spaces"
assert palindrome_check("No 'x' in Nixon") == True, "Error: Failed to ignore quotes and spaces"
assert palindrome_check("Was it a car or a cat I saw?") == True, "Error: Failed to ignore question marks"
assert palindrome_check("12321") == True, "Error: Failed on a numeric palindrome"
assert palindrome_check("123a321") == True, "Error: Failed on alphanumeric palindrome"