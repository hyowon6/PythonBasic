numbers = [1, 2, 3, 4, 5]

del numbers[3:]
print(numbers)


numbers = [1, 2, 3, 4, 5, 3, 2, 9, 10, 3]

# Q1
# output: [1, 2, 4, 5, 3, 2, 9, 10, 3]
numbers.remove(3)
print(numbers)

# Q2
# output: [1, 2, 4, 5, 2, 9, 10]
outputs = []
for num in numbers:
    if num != 3:
        outputs.append(num)

print(outputs)

# 위 구문을 한 문장으로
print([num for num in numbers if num !=3])