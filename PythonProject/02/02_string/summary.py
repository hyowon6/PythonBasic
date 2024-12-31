string = "Step by step goes a long way."

# 문자에 s가 몇 개 있을까
print(string.count('s'))
print(string.index('s'))

# string 쪼개서 list에 저장
print(string.split())
# list 요소를 붙여서 string으로
print(''.join(string.split()))

# input으로 값 받아서 choice 저장
choice = input('Overwrite?(y/n) : ')
print(choice)

# yes, Yes, Y, y
# choice값을 소문자로 받음
# 시작값이 y면 yes로 인식
# 콜론(:) 끝에 꼭 붙여두기
if choice.lower().startswith('y'):
    print('YES')
else:
    print('NO')

string = '  YYYESSS  '
# 오른쪽 공백 제거
print(string.rstrip())

Moon="""
My fellow Koreans, I am grateful to you all. I bow my head in deep appreciation for the choice of you‚ the people. Today‚ serving as President in the 19th presidential term of the Republic of Korea, I take the first step toward a new Korea. My shoulders are now burdened with heavy mandates entrusted to me by the people‚ and my heart is burning with enthusiasm to create the kind of country that we have never been able to live in before. My head is now filled with blueprints for ushering in a new world characterized by unity and coexistence.
"""

# Korea 포함된 단어는 몇개
print(Moon.count('Korea'))
# Korea 단어의 'K'가 나오는 첫번째 index
print(Moon.index('K'))

# 전체 내용을 리스트(list)안에 넣기
# 공백을 중심으로 split
print(Moon.split(' '))
# 문자열(string)로 복원
print(' '.join(Moon.split(' ')))

# Korea 단어를 corea로 변경
print(Moon.replace('Korea', 'corea'))