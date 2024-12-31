file = 'filename.txt'
content = """Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!"""

fd = open(file, 'w')
fd.write(content)
fd.close()

fd = open(file)
while True:
    line = fd.readline()
    if not line:
        break
    print(line, end='')
fd.close()

# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!


# # readline() 함수를 이용하는 경우
fd = open(file)
lines = fd.readlines()
fd.close()

for line in lines:
    print(line, end='')

# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!


fd = open(file)
# 다섯글자만 읽어라
print(fd.read(5))
fd.close

# Hello