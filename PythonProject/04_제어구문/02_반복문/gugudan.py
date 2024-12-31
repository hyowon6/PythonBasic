# 사용자로부터 2~9 사이의 숫자를 입력 받은 후 해당 숫자에 대한 구구단을 출력하는 프로그램

dan = int(input('구구단: '))
for i in range(1,10):
    print('%d x %d = %d'% (dan, i, dan*i))

