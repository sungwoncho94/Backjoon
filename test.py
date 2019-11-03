'''
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
'''
# 답 - 10
'''
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
'''
# 답 - 32

from itertools import combinations

def dist(point1, point2):
    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return distance

def matprint(matrix):
    for a in range(len(matrix)):
        print(matrix[a])

def in_range(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# chicken_list = []
# home_list = []

# for i in range(N):
#     for j in range(N):
#         if matrix[i][j] == 2:
#             chicken_list.append((i, j))
#         if matrix[i][j] == 1:
#             home_list.append((i, j))

# combination_list = list(combinations(chicken_list, M))
# [((0, 1), (3, 0)), ((0, 1), (4, 0)), ((0, 1), (4, 1)), ((0, 1), (4, 4)), ((3, 0), (4, 0)), ((3, 0), (4, 1)), ((3, 0), (4, 4)), ((4, 0), (4, 1)), ((4, 0), (4, 4)), ((4, 1), (4, 4))]

# temp_dist = 0
# min_dist = 9999
# for chic_xy in combination_list:
#     for home_xy in home_list:
#         temp_dist += dist(chic_xy, home_xy)
#     if min_dist > temp_dist:
#         min_dist = temp_dist

# print(min_dist)


a = (1, 1)
b = (2, 2)

print(dist(a, b))
