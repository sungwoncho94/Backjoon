'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''

N, M = map(int, input().split())
matrix = []
for n in range(N):
    m_list = list(map(int, input().split()))
    matrix.append(m_list)

near = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 하, 우, 상, 좌
Q = []

cnt_list = []
year = 0


def bfs():
    cnt = 1
    visit[i][j] = 1
    Q.append((i, j))
    while Q:
        x, y = Q.pop(0)
        for a, b in near:
            xi, yi = (x+a, y+b)
            # 범위를 넘지 않고 방문한적이 없다면 
            if 0 <= xi < N and 0 <= yi < M and visit[xi][yi] == 0:
                # 섬 주변이 바다라면
                if matrix[xi][yi] == 0:# and matrix[x][y] > 0:
                    matrix[x][y] -= 1
                    if matrix[x][y] < 0 :
                        matrix[x][y] = 0 
                # 섬 주변이 또 섬이라면
                elif matrix[xi][yi] > 0:
                    Q.append((xi, yi))   
                    visit[xi][yi] = 1
                    cnt += 1
    return cnt


while len(cnt_list) < 2:
    cnt = 0
    year += 1
    visit = [[0]*M for i in range(N)]
    cnt_list = []
    for i in range(1, N-1):
        for j in range(1, M-1):
            if matrix[i][j] != 0 and visit[i][j] == 0:
                cnt = bfs()    
                cnt_list.append(cnt)
    if cnt == 0:
        year = 1
        break
print(year-1)

