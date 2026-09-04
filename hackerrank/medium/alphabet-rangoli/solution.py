def print_rangoli(size):
    import string
    # Get all lowercase letters
    alpha = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        # Slice letters starting from the outermost character moving inward
        s = "-".join(alpha[size - 1 : i : -1] + alpha[i : size])
        # Center the string using hyphens to fill the total width
        lines.append(s.center(4 * size - 3, "-"))
        
    # Combine the top half, center line, and bottom half symmetrically
    print("\n".join(lines[::-1] + lines[1:]))

