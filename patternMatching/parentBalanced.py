import sys

def parentBalanced(string):
    stack = []
    for char in string:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False

    if stack:
        return False
    return True

if __name__ == "__main__":
    string = sys.argv[1]
    print(string)

    if parentBalanced(string):
        print("Balanced!")
    else:
        print("Not balanced!")