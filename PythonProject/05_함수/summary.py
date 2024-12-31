#!/usr/bin/python3

def char_len_search(l):
    # input: list(citys)
    # output: int(8), int(5)
    # functions:
    # * list(l)를 받아서 글자 수가 큰 값, 글자 수가 작은 값 출력
    # ==> print(l)
    nlist = [len(i) for i in l]
    return max(nlist), min(nlist)

def char_list(l, max, min):
    # input: list(l), int(max), int(min)
    # output: list(longlist), list(shortlist)
    # function:
    # * list와 max, min값을 입력으로 받아서 가장 긴 이름의 list와
    #   가장 작은 이름의 list을 반환한다.
    # ==> print(l, max, min)
    llist = []
    slist = []
    for i in l:
        # ==> print(i, len(i))
        if max == len(i):
            llist.append(i)
        elif min == len(i):
            slist.append(i)

    return llist, slist

def outform(llist, slist):
    # input: list(llist), list(slist)
    # output: None
    # function:
    # Long Name City    : suncheon
    # Short Name City   : seoul, kimpo, pusan
    # ==> print(llist, slist)
    print("Long Name City  :", ''.join(llist))
    print("Short Name City :", ', '.join(slist))

def main():
    citys = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

    # 1) 글자 수가 큰 값, 글자 수가 작은 값 찾기
    # input: list(citys)
    # output: int(8), int(5)
    maxlen, minlen = char_len_search(citys)
    # ==> print(maxlen, minlen)

    # 2) 큰 글자수 list, 작은 글자수 list 출력하기
    # input: list(city), int(maxlen), int(minlen)
    # output: longlist(['suncheon']), shortlist(['seoul', 'kimpo', 'pusan'])
    longlist, shortlist = char_list(citys, maxlen, minlen)
    # ==> print(longlist, shortlist)

    # 3) 출력폼 맞추기
    # input: list(longlist), list(shortlist)
    # output: (출력폼)
    # Long Name City    : suncheon
    # Short Name City   : seoul, kimpo, pusan
    outform(longlist, shortlist)


if __name__ == '__main__':
    main()