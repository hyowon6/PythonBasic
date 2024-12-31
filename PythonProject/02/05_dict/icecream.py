icecream = {'Tankboy': [1200, 5],
            'Pollapo': [1200, 7],
            'Ppangppare': [1800, 6],
            'Worldcorn': [1500, 3],
            'Melona': [1000, 10],
            'Heathunting': [1200, 4]}

# Worldcorn의 희망가격은 어떻게 되나요?
print(icecream['Worldcorn'][0])

# Worldcorn의 남은 수량은?
print(icecream['Worldcorn'][1])

# 남은 수량이 7개 남은 제품 이름은 무엇인가?
for name,rest in icecream.items():
    # print(name, rest[1])
    if rest[1] == 7:
        print(name)

# 희망 가격이 1200원인 제품의 이름과 남은 수량은?
for name,rest in icecream.items():
    # print(name, rest[0])
    if rest[0] == 1200:
        print(name, rest[1])

