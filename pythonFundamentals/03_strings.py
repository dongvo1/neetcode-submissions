visa = "Visa is a payment technology corporation"

len(visa)   # Return length of string
visa[0]     # Return value/character at index 0
visa[0:4]   # Return string from index 0 to 4 --- last index is not inclusive
visa[-1]    # Return last value/character in string
visa[::-1]  # Return string in reverse order
# [start: stop: step]


# String operators
"payment" in visa    # Return True if "payment" is in visa
"money" not in visa  # Return True if "money" is not in visa

# String methods
visa.split()                        # string -> list, splits on spaces by default
"a,b,c".split(",")                  # split on a specific character -> ['a', 'b', 'c']
" ".join(["Visa", "is", "great"])   # list → string, with the separator first: " ".join(words)

