def is_balanced(expression):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}     # Dictionary to map closing to opening brackets

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != bracket_pairs[char]:  # If stack is empty or top of stack doesn’t match, unbalanced
                return False
            stack.pop()

    return not stack   # If stack is empty, it’s balanced

if __name__ == "__main__":
    expressions = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",  # Balanced
        "( 23 ( 2 - 3);",             # Not balanced
        "( 11 }",                     # Not balanced
    ]

    for expr in expressions:
        result = "Symmetric" if is_balanced(expr) else "Not symmetric"
        print(f"Expression: {expr}\nResult: {result}\n")