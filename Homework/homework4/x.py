import collections
x = input("Enter a string: ").lower()
c = collections.Counter(x)
del c[" "]
print(c)