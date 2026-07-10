def first_solution():
    string = input("Type the string : ")
    vowels = [
        'a',
        'e',
        'u',
        'o',
        'i',
    ]

    reversed_string = ''
    vowel_counts = 0
    space_counts = 0
    for i in range(len(string) - 1 , -1, -1):
        reversed_string += string[i]
        if string[i].lower() in vowels:
            vowel_counts += 1
        if string[i] == ' ':
            space_counts += 1

    result = {
        'string': string,
        'vowels': vowel_counts,
        'words': space_counts + 1,
        'reversed': reversed_string
    }
    print(result)

def better_way():
    import json

    text = input("Type the string: ")

    vowel_count = sum(1 for char in text.lower() if char in "aeiou")

    word_count = len(text.split())

    reversed_string = text[::-1]

    result = {
        "vowels": vowel_count,
        "words": word_count,
        "reversed": reversed_string
    }

    print(json.dumps(result, indent=4))


#first_solution()
better_way()