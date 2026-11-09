# List : mutable, can be modify
transactions = [9.99, 20.00, 5.50]

transactions[0]             # Return value at index 0
len(transactions)           # Return length of list
transactions.append(11.00)  # Add element to the back of the list
transactions[0] = 10.00     # Modify the value at index 0
transactions.pop()          # Removes and returns last element
transactions.sort()         # Sort the list in place (same line), return None (dont assign it)
sorted(transactions)        # Return a new sorted list, original unchanged
set(transactions)           # Convert list -> set, remove duplicates

# Tuples : like lists but immutable (cannot be modify), uses () instead of []
card = ("Visa", 6767, 2026)

#card[0] = "Amex"           # Error, tuples cannot be changed
brand, number, year = card  # Unpacking: assigns each element to a variable


# Dictionaries : key -> value pairs (counting)
account = {"name": "Dong", "balance": 100, "is_active": True}

account["name"]             # Return the value for key "name" (KeyError if missing)
account["balance"] = 200    # Change value (dicts are mutable)
account["card"] = "Visa"    # Add a new key -> value pair
account.items()             # Return all (key, value) pairs as tuples
account.get("phone", "N/A") # Return value for key, or default "N/A" if key does not exist (no KeyError)
# Example when to use .get() for counting
word = "banana"
counts = {}

for letter in word:
    counts[letter] = counts.get(letter, 0) + 1

print(counts)   # {'b': 1, 'a': 3, 'n': 2}

"name" in account # True
"Dong" in account # False 
# in checks the keys, not the values


# Sets : Unique values only, with no order (have I seen it)
cards = {"Visa", "Mastercard", "Amex", "Visa"} # Duplicates are removed automatically

cards.add("Discover")   # Add to set (adding to set allows for "seen" pattern)
empty = set()           # Creating an empty set                        
"Visa" in cards         # Return True




