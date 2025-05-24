
from collections import deque

def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    
    char_deque = deque(s)     # Create a deque with the cleaned string
    
    while len(char_deque) > 1:     # Compare characters from both ends
        left = char_deque.popleft()
        right = char_deque.pop()
        if left != right:
            return False

    return True

if __name__ == "__main__":
    test_str = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(test_str):
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")
