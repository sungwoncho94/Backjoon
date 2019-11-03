'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''

def matprint(matrix):
    for a in range(N):
        print(matrix[a])

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


near = [(1, 0), (-1, 0), (0, 1), (0, -1)]
is_zero = 100
hour = 0
cheeze = 99999
temp_cheeze = 0
# 치즈가 남아있다면 계속 돌려야한다
while cheeze > 0:
    hour += 1

    # (1) 밖의 공기를 -1로 바꾸는 bfs -> (0, 0)부터 시작
    i, j = (0, 0)
    matrix[i][j] = -1
    Q = []
    Q.append((i, j))
    visit = [[0]*M for _ in range(N)]
    while Q:    
        x, y = Q.pop(0)
        visit[x][y] = 1
        for a, b in near:
            xi, yi = (x+a, y+b)
            # 범위에 있고, 방문하지 않은 공기층이면 -1씩 빼기
            if 0 <= xi < N and 0 <= yi < M and visit[xi][yi] == 0 and matrix[xi][yi] <= 0:
                Q.append((xi, yi))
                visit[xi][yi] = 1
                matrix[xi][yi] -= 1

    # 치즈를 찾아서 주변에 공기가 있으면(음수면) 녹이기
    cheeze = 0
    result = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                result += 1
                for a, b in near:
                    ai, bj = (i+a, j+b)
                    if 0 <= ai < N and 0 <= bj < M and matrix[ai][bj] < 0:
                        matrix[i][j] = 0
            if matrix[i][j] == 1:
                cheeze += 1

print(hour)
print(result)


