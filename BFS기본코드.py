'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''
N, M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]* M for _ in range(N)]
near = [(1, 0), (0, 1), (0, -1), (-1, 0)]


# bfs
q = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            q.append((i, j))
            visit[i][j] = True
            while q:
                (x, y) = q.pop(0)
                for a, b in near:
                    xi, yi = (x+a, y+b)
                    if 0 <= xi < N and 0 <= yi < M and visit[xi][yi] == False and board[xi][yi] == 0:
                        q.append((xi, yi))
                        visit[xi][yi] = True

