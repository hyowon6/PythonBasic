# 사용자로 부터 4자리의 숫자로 구성된 현관문의 비밀 번호를 입력 받은 후
# 초기 비밀번호와 같은지 체크하는 프로그램

while True:
    secret = input('비밀번호 입력: ')
    if secret == '3415':
        print('맞습니다. 현관문이 열렸습니다.')
        break
    else:
        print('틀렸습니다.\n')
        