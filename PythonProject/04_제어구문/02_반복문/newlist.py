# 파일 이름(확장자 포함) 저장하고 있는 리스트가 있을 때
# 확장자를 제거하고 파일이름만 추가 리스트에 저장하는 프로그램

file_lists = ['hello.py', 'ex01.py', 'ex02.py', 'ch02.py', 'intro.hwp']

output_lists=[]
for file in file_lists:
    output_lists.append(''.join(file.split('.')[:-1]))

print(output_lists)