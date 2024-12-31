# 커피 자판기에 커피는 5개가 들어 있으며 커피 한개의 가격은 300원
# 커피 자판기 이용자가 돈을 넣으면 커피가 남아 있는지 확인하고 없으면 알려줌
# 만약 있다면, 커피를 제공하고 보유한 커피 개수를 줄임
# 커피 자판기에 커피가 더 이상 없으면 이용자에게 알려줌
# + 커피 개수를 사용자가 고르도록

coffee = 5              # 자판기의 커피 개수
while True:
    if not coffee:      # 커피가 없으면
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1     # coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")

    print("남은 커피의 양은 %d개 입니다." % coffee)