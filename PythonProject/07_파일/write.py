file = 'filename.txt'
fd = open(file, 'a')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    fd.write(data)
fd.close()