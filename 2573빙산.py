import copy

def matprint(matrix):
    for n in range(N):
        print(matrix[n])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 최초 0년부터 시작
year = 0

N, M = map(int, input().split())
matrix = []
for n in range(N):
    temp = list(map(int, input().split()))
    matrix.append(temp)

# 주변에 있는 0을 세는 용도. 실제로 값이 -되는건 matrix다.
copy_matrix = copy.deepcopy(matrix)

# visit = 내가 타고 내려온 길로 다시 올라가지 않도록 

# start_idx x, y 찾기
x = y = 0
for n in range(N):
    if x > 0:
        break
    for m in range(M):
        if matrix[n][m] > 0:
            x = n
            y = m
            break

# 빙산 녹이기
for i in range(N):
    for j in range(N):
        if matrix[i][j] > 0:
            for d in range(4):
                if copy_matrix[i+dx[d]][j+dy[d]] == 0:
                    matrix[i][j] -= 1
                    if matrix[i][j] < 0:
                        matrix[i][j] = 0
# matprint(matrix)
# copy_matrix 바꿔주기
copy_matrix = copy.deepcopy(matrix)


# 섬의 개수
cnt = 0

