def recursive_str_len(s):
    """
    Recursively calculates the length of a string.
    
    Args:
    s (str): The input string
    
    Returns:
    int: The length of the string
    """
    # Base case: empty string
    if s == "":
        return 0
    # Recursive case: remove first character and add 1
    else:
        return 1 + recursive_str_len(s[1:])
        