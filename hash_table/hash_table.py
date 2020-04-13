book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["orange"] = 1.49
print(book)
print(book["apple"])

# -------------------------------

phone_list = {}
phone_list["Jenny"] = 845337
phone_list["Emergency"] = 911
print(phone_list["Jenny"])

# -------------------------------

voted = {}
def voter_checks(name):
    if voted.get(name):
        print("Cannot vote")
    else:
        voted[name] = True
        print("Can vote!")

print(voter_checks("Tom"))
print(voter_checks("Mike"))
print(voter_checks("Mike"))