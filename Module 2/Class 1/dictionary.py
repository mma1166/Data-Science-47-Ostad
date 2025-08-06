# guest = {"name":"Alice", "Age": 25, "favourite_snack": "cake"}

# #Let's see the guest's name:

# print("Guest name:", guest["name"])
# print("Guest's Age:", guest["Age"])

# #Let's add favourite color:

# guest["favourite_color"]="Orange"

# print("guest's favourite color:",guest["favourite_color"])
# print(guest)

# del guest["Age"]
# print(guest)

# guest.pop("age")
# print(guest)

# for key,val in guest.items():
#     print(key,val)
#     print(key)
#     print(val)

party_guest= {
    "guest1":{"name":"Alice", "favourite_snack":"cake"},
    "guest2":{"name":"Sunny", "favourite_snack":["chips","choco"]}
}
print(party_guest["guest2"])
print(party_guest["guest2"]["favourite_snack"])
print(party_guest["guest2"]["favourite_snack"][0])