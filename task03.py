def is_palindrome(input_string):
    stack = []
    opening_br = "({["
    closing_br = ")}]"
    matching_br = {')': '(', '}': '{', ']': '['}
    
    for char in input_string:
        if char in opening_br:
            stack.append(char)
        elif char in closing_br:
            if not stack:
                return "Несиметрично"
            top_char = stack.pop()
            if matching_br[char] != top_char:
                return "Несиметрично"
    
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"

test1 = "( ){[ 1 ]( 1 + 3 )( ){ }})"
test2 = "( 23 ( 2 - 3);)"
test3 = "( 11 })"
    
print(is_palindrome(test1))  
print(is_palindrome(test2))   
print(is_palindrome(test3))    