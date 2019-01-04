fr = ['banana', 'apple', 'orange', 'pear']
pr = [4, 2, 1.5, 3]
st = [6, 0, 32, 15]
# Creat dict prices, stock
prices = {}
stock = {}
for i, j in enumerate(fr):
    prices[j] = pr[i]
    stock[j] = st[i]
# Print price and stock
for key in prices:
    print(key)
    print('price', prices[key], sep=': ')
    print('stock', stock[key], sep=': ')
    print('----------------------------')
# Calculate money
total = 0
worth ={}
for key in prices:
    total += prices[key]*stock[key]
    worth[key] = prices[key]*stock[key]
print("Worth of each product: ")
print(worth)
print("Total worth of all product: ",total)