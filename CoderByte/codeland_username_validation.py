import re

def codeland_username_validation(text: str) -> bool:
    if not (4 <= len(text) <= 25):
        return False
    
    if not text[0].isalpha():
        return False
    
    if text.endswith('_'):
        return False
    
    if not all(char.isalnum() or char == '_' for char in text):
        return False

    return True

def clean_regex(text: str) -> bool:
    # 1. Check length explicitly (regex can do this, but checking length first is faster)
    if not (4 <= len(text) <= 25):
        return False
    
    # 2. Match the pattern:
    # ^[a-zA-Z]        -> Must start with a letter
    # [a-zA-Z0-9_]* -> Followed by 0 or more valid characters
    # [a-zA-Z0-9]$     -> Must end with a letter or number (no underscore)
    pattern = r"^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]$"
    
    # re.match returns a Match object if true, or None if false
    return bool(re.match(pattern, text))

assert codeland_username_validation("user") is True
assert codeland_username_validation("User123") is True
assert codeland_username_validation("user_name") is True
assert codeland_username_validation("A123") is True
assert codeland_username_validation("a_b_c_d") is True
assert codeland_username_validation("abcdefghijklmnopqrstuvwxy") is True
assert codeland_username_validation("abc") is False
assert codeland_username_validation("abcdefghijklmnopqrstuvwxyz") is False
assert codeland_username_validation("1user") is False
assert codeland_username_validation("_user") is False
assert codeland_username_validation("user_") is False
assert codeland_username_validation("user-name") is False
assert codeland_username_validation("user name") is False
assert codeland_username_validation("user!") is False
assert codeland_username_validation("user@123") is False
assert codeland_username_validation("A___") is False
assert codeland_username_validation("A__1") is True
assert codeland_username_validation("Z999999999999999999999999") is True
assert codeland_username_validation("") is False

assert clean_regex("user") is True
assert clean_regex("User123") is True
assert clean_regex("user_name") is True
assert clean_regex("A123") is True
assert clean_regex("a_b_c_d") is True
assert clean_regex("abcdefghijklmnopqrstuvwxy") is True
assert clean_regex("abc") is False
assert clean_regex("abcdefghijklmnopqrstuvwxyz") is False
assert clean_regex("1user") is False
assert clean_regex("_user") is False
assert clean_regex("user_") is False
assert clean_regex("user-name") is False
assert clean_regex("user name") is False
assert clean_regex("user!") is False
assert clean_regex("user@123") is False
assert clean_regex("A___") is False
assert clean_regex("A__1") is True
assert clean_regex("Z999999999999999999999999") is True
assert clean_regex("") is False

print("All tests passed!")