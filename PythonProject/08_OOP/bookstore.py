class Book:
    # 초깃값 생성
    def __init__(self, title, price, author):
        print('책 객체가 새로 만들어졌습니다.')
        self.setData(title, price, author)

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('제목: ', self.title)
        print('가격: ', self.price)
        print('작가: ', self.author)

b = Book('내가 먹었지롱', '200원', '미니')
b.printData()

