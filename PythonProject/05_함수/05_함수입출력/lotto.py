# 로또 번호 생성기 프로그램
# random 모듈의 ranint를 사용하여 6개의 로또 번호를 생성하는 lotto_number() 함수
# 숫자는 1~45까지 존재하며 중복된 숫자는 나올 수 없음
# lotto_number() 함수는 매개변수로 뽑고 싶은 로또 번호 개수를 지정하도록 구성
# 예를 들어, 6을 지정하면 로또 번호 6개를 랜덤하게 뽑음

import random

lotto_numbers = []
for i in range(1, 46):
    lotto_numbers.append(i)

def lotto_number(num):
    # input: int(num)
    # output: 숫자 6개(1~45 사이)
    # function: 로또 번호 생성기

    choiced_num = []
    for i in range(num):
        # 2. 번호 섞기
        random.shuffle(lotto_numbers)
        # print(lotto_numbers)

        # 1. 뽑으려는 숫자
        max = len(lotto_numbers)
        choice = random.randint(0, max-1)
        # print(choice)

        # 3. 번호 추출하기
        lotto_num = lotto_numbers.pop(choice)
        # print(lotto_num)
        choiced_num.append(lotto_num)

    print(' '.join(str(choiced_num)))

def main():
    lotto_number(6)

main()







