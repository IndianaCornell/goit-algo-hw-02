from collections import deque

def is_palindrome(string):
    string = string.replace(" ", "").lower()
    char_deque = deque()

    for char in string:
        char_deque.append(char)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


str = "TENET"
print(is_palindrome(str))   