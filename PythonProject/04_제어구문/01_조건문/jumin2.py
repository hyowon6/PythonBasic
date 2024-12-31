
j = input('주민등록번호: ')
#    234567 892345
# j = '821010-1635210'
#    012345 789012

### 1. 1st
first = int(j[0])*2 + int(j[1])*3 + int(j[2])*4 + \
        int(j[3])*5 + int(j[4])*6 + int(j[5])*7 + \
        int(j[7])*8 + int(j[8])*9 + int(j[9])*2 + \
        int(j[10])*3 + int(j[11])*4 + int(j[12])*5
# print(first)

### 2. 2nd
second = first % 11
# print(second)

### 3. 3th
chksum = 11 - second

if chksum == int(j[13]):
    print('[ OK ] 유효합니다.')
else:
    print('[ FAIL ] 유효하지 않습니다.')