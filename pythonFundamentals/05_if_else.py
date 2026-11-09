# if / elif / else

balance = 50
account = "Dong"

if balance > 100:
    print("rich")
elif balance >= 50:
    print("okay")
else:
    print("broke")


# logical
if balance >= 40 and account == "Dong":
    print("good")

# Truthiness
nums = []
if not nums:
    print("Empty")
