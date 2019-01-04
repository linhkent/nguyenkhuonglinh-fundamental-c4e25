#person['Quan',25,'Hanoi',3,False,125]
person = {
    "name": "Quan",
    "age": 25,
    "location": "Hanoi",
    "exes": 3,
    "status": False,
    "friends": 125
}
person["name"] = "A Quan"
person["exp"] = 2
del person["exes"]
print(person)
