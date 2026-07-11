def compress(text: str) -> str:
    if not text:
        return ""

    parts = []
    previous = text[0]
    count = 1

    # Start from index 1
    for char in text[1:]:
        if char == previous:
            count += 1
        else:
            parts.append(f"{previous}{count}")
            previous = char
            count = 1

    parts.append(f"{previous}{count}")
    return "".join(parts)

assert compress("") == ""
assert compress("a") == "a1"
assert compress("aa") == "a2"
assert compress("ab") == "a1b1"
assert compress("abc") == "a1b1c1"
assert compress("aaa") == "a3"
assert compress("aaabbc") == "a3b2c1"
assert compress("aabcccccaaa") == "a2b1c5a3"
assert compress("wwwwaaadexxxxxx") == "w4a3d1e1x6"
assert compress("111222") == "1323"
assert compress("AAaa") == "A2a2"
assert compress("ababab") == "a1b1a1b1a1b1"
assert compress("zzzzzzzzzz") == "z10"
assert compress("aabbaa") == "a2b2a2"
assert compress("   ") == " 3"
assert compress("!!@@@###") == "!2@3#3"