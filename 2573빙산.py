'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''

def matprint(matrix):
    for a in range(len(matrix)):
        print(matrix[a])

N, M = map(int, input().split())
matrix = []
for n in range(N):
    m_list = list(map(int, input().split()))
    matrix.append(m_list)

# 가지 않은 곳 = 0 / 방문한 곳 = 1
visit = [[0]*M for i in range(N)]
near = [(1, 0), (0, 1), (-1, 0), (0, -1)]
Q = []
island = 0  # 섬의 개수
cnt = 0  # 몇 번 count 해야하는지?

# 배열을 탐색하며 섬이 시작되는 곳에서 BFS시작한다
for i in range(N):
    for j in range(M):
        if matrix[i][j] > 0:
            # BFS 기본준비 / 시작점 visit표시, Q에 등록
            visit[i][j] = 1
            Q.append((i, j))
            # BFS 시작 / Q가 빌 때까지
            while Q:
                x, y = Q.pop(0)
                # 사방탐색
                for a, b in near:
                    xi, yi = (x+a, y+b)
                    # 현재위치 i, j에서 사방으로 탐색하며 갈 수 있는 곳이 있다면, Q에 등록하고 visit = 1로 바꾼다. 또한, 현재에서 방문할 수 있는
                    # matrix 범위를 넘지 않고, visit한 적이 없으며
                    if visit[xi][yi] == 0 and 0 <= xi < N and 0 <= yi < M:
                        # 주변이 바다이면 자신을 -= 1 해주기 (최대 0까지만)
                        if matrix[xi][yi] == 0 and matrix[x][y] > 0:
                            matrix[x][y] -= 1
                        # 주변이 방문할 수 있는 섬이라면,
                        elif  matrix[xi][yi] > 0:
                            Q.append((xi, yi))
                            visit[xi][yi] = 1
                            x, y = (xi, yi)
            # Q가 끝났으면 섬 하나 탐색을 끝낸 것.
            cnt += 1  # cnt 증가
            



