import re

def palindrome_check(text: str) -> bool:
    # Regular Expression
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text)
    reversed_text = cleaned[::-1]
    return cleaned.lower() == reversed_text.lower()

def memory_friendly(text: str) -> bool:
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text)
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left].lower() != cleaned[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

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

assert memory_friendly("") == True, "Error: Failed on empty string"
assert memory_friendly("a") == True, "Error: Failed on single character"
assert memory_friendly("   ") == True, "Error: Failed on string with only spaces"
assert memory_friendly("racecar") == True, "Error: Failed on a basic lowercase palindrome ('racecar')"
assert memory_friendly("hello") == False, "Error: Failed on a basic non-palindrome ('hello')"
assert memory_friendly("RaceCar") == True, "Error: Failed to ignore case ('RaceCar')"
assert memory_friendly("Level") == True, "Error: Failed to ignore case ('Level')"
assert memory_friendly("A man, a plan, a canal: Panama") == True, "Error: Failed on complex punctuation/spaces"
assert memory_friendly("No 'x' in Nixon") == True, "Error: Failed to ignore quotes and spaces"
assert memory_friendly("Was it a car or a cat I saw?") == True, "Error: Failed to ignore question marks"
assert memory_friendly("12321") == True, "Error: Failed on a numeric palindrome"
assert memory_friendly("123a321") == True, "Error: Failed on alphanumeric palindrome"