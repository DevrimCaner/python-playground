def question_marks(text):
    last_digit = None
    last_index = -1
    found_pair = False
    
    for i, char in enumerate(text):
        if char.isdigit():
            current_digit = int(char)
            
            if last_digit is not None and last_digit + current_digit == 10:
                found_pair = True
                
                question_mark_count = text[last_index:i].count('?')
                
                if question_mark_count != 3:
                    return False
            
            last_digit = current_digit
            last_index = i

    return found_pair
  
assert question_marks("5???5") == True, "Failed on a basic single valid pair"
assert question_marks("arrb6???4xxbl5???5") == True, "Failed on multiple valid pairs"
assert question_marks("9???1???9") == True, "Failed on successive valid pairs"
assert question_marks("5??5") == False, "Failed to catch a pair with only 2 question marks"
assert question_marks("5????5") == False, "Failed to catch a pair with 4 question marks"
assert question_marks("6???4xyz55") == False, "Failed to catch a failing second pair"
assert question_marks("3???5") == False, "Incorrectly approved a pair that doesn't sum to 10"
assert question_marks("abc???asd") == False, "Incorrectly approved a string with no numbers"
assert question_marks("") == False, "Failed on empty string"
assert question_marks("5") == False, "Failed on a single digit string"
assert question_marks("???") == False, "Failed on a string with only question marks"

print("All tests passed!")