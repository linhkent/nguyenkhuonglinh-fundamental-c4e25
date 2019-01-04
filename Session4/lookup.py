dicts = {
    "go" : "đi",
    "come": "đến",
    "stay": "ở lại",
    "move": "di chuyển"
}
print('Search: ')
print(dicts.keys())
a = input()
if a in dicts:
    print(dicts[a])
    e = input("Want to update?: ").lower()
    if e == 'y':
        dicts[a] = input("New: ")
        print(dicts)
else:
    e = input("Not exits, want to update?: ").lower()
    if e == 'y':
        dicts[a] = input("New: ")
        print(dicts)
