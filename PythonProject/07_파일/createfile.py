import os

if not os.path.exists('test.txt'):
    os.mkdir('/test', ' ', ' ')
    print('The file is removed.')

contents = """반갑습니다. 파이썬 개발자 여러분
한살 더 드셨죠!
올 한해는 행복한 가득한 한해가 되었으면 합니다.
"""

with open('test.txt', 'w') as fd:
    fd.write(contents)

with open('test.txt') as fd:
    print(fd.read())

if os.path.exists('test.txt'):
    os.remove('test.txt')
    print('The file is removed.')
