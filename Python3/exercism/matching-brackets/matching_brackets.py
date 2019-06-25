# Define the bracked signs with open as key and closing as value.
SIGNS = {
    '(': ')',
    '[': ']',
    '{': '}'
    }


def is_paired(input_string):
    # Define a stack of currently open brackets.
    open_stack = []

    # Iterate for characters in input_string.
    for char in input_string:
        # Check if it's an opening bracket.
        if char in SIGNS.keys():
            open_stack.append(char)
        # Check if it's a closing bracket.
        elif char in SIGNS.values():
            # Find the key, that has the value of the closing bracket.
            for key, value in SIGNS.items():
                if value == char:
                    open_char = key
                    break
            # Check if there is anything to close, and whether it's closing the
            # most recently opened bracket.
            if not open_stack or open_stack[-1] != open_char:
                return False
            # Remove the top value from the stack.
            open_stack.pop(-1)

    return not open_stack
