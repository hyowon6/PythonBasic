# 1) string
str1 = 'Hello World'

for i in str1:
	print(i)

# 2) list
list1 = ['a', 'b', 'c', 'd', [1, 2, 3]]

for i in list1:
	print(i)

# 3) tuple
tuple1 = ('a', 'b', 'c', [1, 2, 3])

for i in tuple1:
	print(i)

# 4) dict
dict1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

for k,v in dict1.items():
	print(k,v)

# 5) set
set1 = {'a', 'b', 'c'}

for i in set1:
	print(i)
