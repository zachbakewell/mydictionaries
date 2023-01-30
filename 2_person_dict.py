person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
second_child = person["children"][1]
print(second_child)


# print out the name of the cat
cat = person["pets"]['cat']
print(cat)


# iterate through all children and print out each child
for child in person["children"]:
    print(child)


# print out the pets in this format:
# type of pet: dog name of pet: Fido
for pet,name in person["pets"].items:
    print(f'Type of pet: {pet} Name of pet: {name}')