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

near = [(1, 0), (0, 1), (-1, 0), (0, -1)]
Q = []
# island = 0  # 섬의 개수
# cnt = 0  # 몇 번 count 해야하는지?
flag = 1

# while island <= 1 and flag ==1:

cnt_list = []
while len(cnt_list) < 2:
    # cnt_list 가 새로 생길 때마다 visit 새로 생성
    visit = [[0]*M for i in range(N)]

    for i in range(1, N):
        for j in range(1, M):
            # 섬의 시작부분에서 cnt += 1
            if matrix[i][j] > 0 and visit[i][j] == 0:
                cnt = 1
                visit[i][j] = 1
                Q.append((i, j))
            
                while Q:
                    #matprint(matrix)
                    x, y = Q.pop(0)
                    for a, b in near:
                        xi, yi = (x+a, y+b)
                        # 범위를 넘지 않고 방문한적이 없다면 
                        if 0 <= xi < N and 0 <= yi < M and visit[xi][yi] == 0:
                            # 섬 주변이 바다라면
                            if matrix[xi][yi] == 0 and matrix[x][y] > 0:
                                matrix[x][y] -= 1
                            # 섬 주변이 또 섬이라면
                            elif  matrix[xi][yi] > 0:
                                Q.append((xi, yi))
                                visit[xi][yi] = 1
                                cnt += 1
                
                # Q가 끝날 때 마다 -> 섬 하나가 끝날 때마다 cnt_list에 섬 크기 추가
                cnt_list.append(cnt)
print(len(cnt_list))


