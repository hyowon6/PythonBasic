
# Q1: 문자열 길이
# mystring이라는 문자열의 길이를 출력하는 프로그램을 구현하라.
mystring = "hello world"
print("mystring's length =", len(mystring))

# Q2: 문자열 분리
# 영상의 크키를 my_resolution이 바인딩하고 있을 때, 영상의 너비와 높이를 출력하라.
# 예를 들어, '176x144'이면 너비가 176, 높이가 144 이다.
my_resolution = '1920x1080'
print(my_resolution.split('x'))
print("width  =", my_resolution.split('x')[0])
print("height =", my_resolution.split('x')[1])

# Q3: 문자열 합치기
# 리스트에 회사 이름이 저장되어 있다.
# 각 회사 이름이 구분자 ";"로 연결된 문자열을 생성하라.
companies = ['NAVER', 'KAKAO', 'SK', 'SAMSUNG']
companystring= ';'.join(companies)
print(companystring)

# Q4: 도메인 추출
# 사용자로부터 웹페이지 주소를 입력 받은 후 도메인을 출력하라.
# 도메인은 .com, .net, .org 만 지원한다. www는 반드시 입력된다.
# url = 'http://www.naver.com/edit/page/7022'
url = input('address: ')
print("domain: ", url.split(':')[1].split('/')[2].split('.')[-1])

# Q5: 문자열 자르기
# 사용자로 부터 파일명을 입력 받은 후 확장자만 출력하는 프로그램
file = input('filename: ')
print(file.split('.')[-1])

# 경로 분리
# 사용자로 부터 윈도우 디렉토리를 입력 받은 후 가장 최종 디렉토리를 출력하라.
file = input('Path: ')
print(file.split('/'))

filename_split_list = file.split('/')
print("path    :", '/'.join(filename_split_list[:-1]))
print("filename:", filename_split_list[-1])

