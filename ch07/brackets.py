"""
File: brackets.py
"""

from stack import LinkedStack


def bracketBalance(exp):
    """exp represents the expression"""
    stk = LinkedStack()         # Create a new stack
    for ch in exp:              # Scan across the expression
        if ch in ['[', '(']:    # Push an opening bracket
            stk.push(ch)
        elif ch in [']', ')']:
            if stk.isEmpty():   # Not balanced
                return False
            chFromStack = stk.pop()
            # Brackets must be of same type and match up
            if ch == ']' and chFromStack != '[' or \
               ch == ')' and chFromStack != '(':
                return False
    return stk.isEmpty()        # They all matched up


def main():
    exp = raw_input("Enter a bracketed expression: ")
    if bracketBalance(exp):
        print "OK"
    else:
        print "Not OK"


main()
