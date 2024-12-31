import time

class Coffee:
    total_amount = 10           # 자판기 커피 수량
    total_amount_price = 5000   # 자판기 돈
    coffee_price = 300          # 커피 가격
    put_price = 0               # 넣은 금액
    req_coffee_nums = 0         # 요청 개수
    remaining_price = 0         # 거스름 돈
    remaining_coffee_nums = 0   # 출력 개수

    # 사용자로부터 돈과 원하는 커피 개수를 입력받는 동작
    def request(self):
        self.req_coffee_nums = int(input('몇 잔 드릴까요? '))
        self.put_price = int(input('돈을 넣어주세요: '))

    # 커피를 뽑는 동작
    def get(self):
        # 거스름돈 계산
        self.remaining_price = (self.put_price - (self.coffee_price * self.req_coffee_nums))
        print('\n--계산 중--')

        # 거스름 돈이 있는 경우(EX: 700원, 2개 요청)
        if self.remaining_price > 0 and self.total_amount > self.req_coffee_nums:
            # 돈 받기
            self.total_amount_price += self.put_price
            # 커피 개수 차감
            self.total_amount -= self.req_coffee_nums
            # 거스름돈 차감
            self.total_amount_price -= self.remaining_price
            print('거스름 돈입니다: %d원' %self.remaining_price)
            print('커피 %d잔 나왔습니다. 맛있게 드세요~\n' % self.req_coffee_nums)

        # 거스름 돈이 없는 경우(EX: 600원, 2개 요청)
        elif self.remaining_price == 0 and self.total_amount > self.req_coffee_nums:
            # 돈 받기
            self.total_amount_price += self.put_price
            # 커피 개수 차감
            self.total_amount -= self.req_coffee_nums
            # 거스름 돈 차감
            self.remaining_price = 0
            print('커피 %d잔 나왔습니다. 맛있게 드세요~\n' % self.req_coffee_nums)

        # 커피 수량이 부족할 때(EX: 5000원, 11개 요청)
        elif self.total_amount < self.req_coffee_nums:
            print('지금 가능한 커피 수량은 %d잔입니다.\n' % self.total_amount)
            # 초기화
            self.req_coffee_nums = 0
            self.remaining_price = self.put_price

        # 돈이 부족한 경우(EX: 500원, 2개 요청)
        elif self.remaining_price < 0:
            print('돈이 %d원만큼 부족합니다.\n' %self.remaining_price)
            # 초기화
            self.req_coffee_nums = 0
            self.remaining_price = self.put_price

        else:
            print(' ')

    # 손님 상황
    def info(self):
        time.sleep(1)
        print('--손님--')
        print('지갑:', self.remaining_price)
        print('커피:', self.req_coffee_nums, '\n')


    # 현재 자판기에 남은 돈과 남아있는 커피 개수 점검
    def check_amount(self):
        print('--자판기--')
        print('수량:', self.total_amount)
        print('금액:', self.total_amount_price)
        time.sleep(1)
        if self.total_amount <= 0 or self.total_amount_price <= 0:
            print('작동 중지')
        else:
            print(' ')

customer = Coffee()
customer.request()
customer.get()
customer.info()
customer.check_amount()




