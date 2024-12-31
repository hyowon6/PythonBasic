# 도시 이름을 저장하고 있는 리스트가 있을 때,
# 이름이 가장 긴 도시 이름과 가장 짧은 도시 이름을 출력하는 프로그램

citys = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

citys_len = [len(i) for i in citys]
max_citys_len = max(citys_len)
min_citys_len = min(citys_len)

long_name_city = []
short_name_city = []
for city in citys:
    if len(city) == max_citys_len:
        long_name_city.append(city)
    else len(city)