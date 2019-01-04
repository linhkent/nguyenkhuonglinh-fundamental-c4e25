inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
# Add key 'pocket'
inventory['pocket'] =[]
print(inventory)
# Set the value of 'pocket'
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)
# remove 'dagger' from 'back pack' key
inventory['backpack'].remove('dagger')
print(inventory)
# add 50 to the number stored under the 'gold' key 
inventory['gold'] += 50
print(inventory)