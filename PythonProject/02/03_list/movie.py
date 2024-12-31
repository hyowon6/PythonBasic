movies = {'파묘': [23.6, 5.5, 11914798],
          '범죄도시4': [20.6, 8.8, 11502779],
          '인사이드 아웃2': [15.6, 8.8, 7525302],
          '베테랑2': [10.8, 5.3, 5000000]}

# 파묘의 관객 수?
print(movies['파묘'][2])

# 평점이 8.8인 영화 제목은?
for movie in movies:
    # print(movie, movies[movie][1])
    if movies[movie][1] == 8.8:
        print(movie)

# 관객 수가 1000만명 이상이 되는 영화 제목
for movie in movies:
    # print(movie, movies[movie][2])
    if movies[movie][2] > 10000000:
        print(movie)