# for loop

transactions = [9.99, 20.00, 5.50]

for i in transactions:
    print(i)

for i in range(0, 10, 2): # (start, stop, step) -> stop not included
    print(i)

for i in range(len(transactions)):
    print(i,transactions[i])  # print index and value

for i, t in enumerate(transactions): 
    print(i, t)


# while loop
balance = 100

while balance > 0:
    balance -= 10
    print(balance)

# break/continue