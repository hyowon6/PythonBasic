# 아파트의 각 집마다 배달해야 하는 우유의 개수를 딕셔너리로 표현
# 해당 딕셔너리를 사용하여 각 집마다 배달해야 하는 우유와 그 개수를 출력하는 프로그램

milk_orders = {'101': {'milk':1, 'yogurt': 5},
               '102': {'milk':2},
               '103': {'milk': 1, 'yogurt': 10},
               '104': {'yogurt': 15}}

for ho,order in milk_orders.items():
    if order.get('milk'):
        print("%s 호 milk : %d개" % (ho, order['milk']))