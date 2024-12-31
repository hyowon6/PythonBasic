class Fridge:
    # 속성(property)
    # 냉장고 문이 열렸는지 닫혔는지
    isOpened = False
    # 냉장고 안의 음식
    foods = []

    # 메소드(method)
    # 냉장고 문 열기
    def open(self):
        self.isOpened = True
        print('[  OK  ] 냉장고 문이 열렸습니다.')

    # 냉장고 문이 열렸으면 음식을 넣고,
    # 냉장고 문이 닫혀있다면 에러 출력
    def put(self, things):
        if self.isOpened:
            self.foods.append(things)
            print('[  OK  ] 냉장고에 %s을 넣었습니다.' % things)
        else:
            print('[ FAIL ] 냉장고 문이 닫혀 있습니다.')

    # 냉장고 문 닫기
    def close(self):
        self.isOpened = False
        print('[  OK  ] 냉장고 문을 닫았습니다.')


class Food:
    pass