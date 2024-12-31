import sys

# 사용자로 부터 휴대전화 번호를 입력 받은 후 통신사를 출력하는 프로그램
# (단, 통신사를 확인하고 출력하는 communication() 함수)
# 다음은 통신사에 대한 정보
# 011 : SKT, 016 : KT, 019 : LGT, 010 : 알수없음

def communication(number):
    # input: str(011,019,017,016,010, ...)
    # output: str(SKT, KT, LGT, UNKNOWN)
    if number == '011':
        RET = 'SKT'
    elif number == '016':
        RET = 'KT'
    elif number == '019':
        RET = 'LGT'
    elif number == '010':
        RET = 'UNKNOWN'
    else:
        RET = 'UNKNOWN'
    return RET

phone_number = input("휴대전화번호 입력: ")
first = phone_number.split('-')[0]
comm = communication(first)

if   comm == 'SKT'   : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'KT'    : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'LGT'   : print('당신은 %s 사용자입니다.' % comm)
elif comm == 'UNKOWN': print('당신의 통신사는 알수 없습니다.')
else: sys.exit(1)