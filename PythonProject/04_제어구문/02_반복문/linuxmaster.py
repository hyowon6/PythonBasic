# 시험 정수가 marks list에 들어 있음
# 커트라인은 60점
# 학생들의 합격/불합격 여부를 판단하는 프로그램
marks = [90, 25, 67, 45, 80]

for i, mark in enumerate(marks):
    num = i+1
    if mark >= 60:
        print('%d번 학생: 합격' % num)
    else:
        print('%d번 학생: 불합격' % num)
