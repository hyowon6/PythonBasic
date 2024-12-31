import sys

# 사용자로부터 점수를 입력 받은 후 등급을 출력
# 등급표(A: 81~100, B: 61~80, C: 41~60, D: 21~40, E: 0~20)
score = int(input('Score: '))
if 100 >= score > 81:
    print('grade is A')
elif 80 >= score >= 61:
    print('grade is B')
elif 60 >= score >= 41:
    print('grade is C')
elif 40 >= score >= 21:
    print('grade is D')
elif 20 >= score >= 0:
    print('grade is E')
else:
    print('[ FAIL ] 잘못된 점수 입력입니다.')
    sys.exit(1)

