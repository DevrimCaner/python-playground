import string

def longest_word(text: str) -> str:
    result = ""
    
    for word in text.split():
        clean_word = word.strip(string.punctuation)
        if len(clean_word) > len(result):
            result = clean_word

    return result

assert longest_word("") == "", "Failed on empty string"
assert longest_word("     ") == "", "Failed on string with only spaces"
assert longest_word("I love programming in Python") == "programming", "Failed on standard sentence"
assert longest_word("The quick brown fox jumps") == "quick", "Failed on tie-breaker"
assert longest_word("Python") == "Python", "Failed on single word input"
assert longest_word("Hello, universe!") == "universe", "Failed to handle punctuation properly"
assert longest_word("A confusing... sentence?!") == "confusing", "Failed on heavy punctuation"
assert longest_word("  Space   frontier  ") == "frontier", "Failed on irregular spacing"
assert longest_word("My favorite number is 1234567890") == "1234567890", "Failed on numeric words"