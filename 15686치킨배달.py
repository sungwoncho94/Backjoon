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


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
chicken_list = []
home_list = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            chicken_list.append((i, j))
        if matrix[i][j] == 1:
            home_list.append((i, j))

combination_list = list(combinations(chicken_list, M))
# [((0, 1), (3, 0)), ((0, 1), (4, 0)), ((0, 1), (4, 1)), ((0, 1), (4, 4)), ((3, 0), (4, 0)), ((3, 0), (4, 1)), ((3, 0), (4, 4)), ((4, 0), (4, 1)), ((4, 0), (4, 4)), ((4, 1), (4, 4))]

min_dist = 0
result = 9999999
for comb in combination_list:  # ((0, 1), (3, 0))  // N개의 치킨집 고른 것
    for home_xy in home_list:  # [(0, 3), (1, 0), (1, 2), (3, 3), (3, 4), (4, 3)]
        temp_dist = 9999
        for chic_xy in comb:  # (0, 1) / (3, 0)
            # 집 하나마다(home_xy) 거리가 짧은 치킨집이 정해짐
            if dist(home_xy, chic_xy) < temp_dist:
                temp_dist = dist(home_xy, chic_xy)
        # list의 치킨집 중 거리가 짧은 치킨집이 구해지면 그걸 더한다
        min_dist += temp_dist
    if result > min_dist:
        result = min_dist
print(result)

'''
하고싶은 것
치킨집 2개를 뽑았고, 조합을 구했다.
치킨집1 - 집1 vs 치킨집2 - 집1 의 거리를 비교해서 짧은 것만 temp_dist에 더한다
총 temp_dist가 나왔으면 min_dist와 비교하면 최종 min_dist를 구한다
'''