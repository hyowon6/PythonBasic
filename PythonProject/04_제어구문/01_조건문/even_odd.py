
# 사용자로 부터 2개의 숫자를 입력 받은 후
num1 = int(input('num1 입력: '))
num2 = int(input('num2 입력: '))

# 큰 숫자를 화면에 출력
if num1 > num2:     bignum = num1
elif num1 < num2:   bignum = num2
else:               bignum = '같음'

print('큰 수:', bignum)

# 큰 숫자가 홀수(odd)인지 짝수(even)인지 출력
if (bignum % 2) == 0:    even = '짝수'
else:                    even = '홀수'

print('짝홀수:', even)