
# 지역 번호 구별 함수
def region_fun(region):
    if 0 <= region <= 8:
        print('지역: 서울')
    elif 9 <= region <= 12:
        print('지역: 부산')
    elif 13 <= region <= 15:
        print('지역: 인천')
    elif 16 <= region <= 25:
        print('지역: 경기도')
    elif 26 <= region <= 34:
        print('지역: 강원도')
    elif 35 <= region <= 39:
        print('지역: 충청북도')
    elif region == 40:
        print('지역: 대전광역시')
    elif 41 <= region <= 47:
        print('지역: 충청남도')
    elif 48 <= region <= 55:
        print('지역: 전라북도')
    elif 56 <= region <= 64:
        print('지역: 전라남도')
    elif 65 <= region <= 66:
        print('지역: 광주광역시')
    elif 67 <= region <= 69:
        print('지역: 대구광역시')
    elif 70 <= region <= 80:
        print('지역: 경상북도')
    elif (81 <= region <= 99) and (region != 85):
        print('지역: 경상남도')
    elif region == 85:
        print('지역: 울산광역시')
    else:
        print('지역: 혹시 외국인!!')

# 주민번호 입력 받기
j = input('주민등록번호: ')

# 성별
gender = j[7]
if gender == '1' or gender == '3':
    g = '남자'
elif gender == '2' or gender == '4':
    g = '여자'
print('성별:', g)

# 지역
region = int(j[8:10])
region_fun(region)

