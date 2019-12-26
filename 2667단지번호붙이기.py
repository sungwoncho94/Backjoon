def print_mat(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

# i, j가 범위 안에 있으면서 1일 때만 갈 수 있는 길로 지정한다
def is_ok(i, j):
    if 0 <= i < N and 0 <= j < N and matrix[i][j] == '1':
        return True
    return False

N = int(input())
m_list = [str(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
matrix = []

# 단지가 나올 때 마다, 각 단지의 개수를 여기에 append하기
result_list = []

# 하, 우, 상, 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    t_list = m_list[i]
    temp_list = []
    for t in t_list:
        temp_list.append(t)
    matrix.append(temp_list)

for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1':
            # 넓이 우선 탐색인 BFS & Q를 사용한다
            Q = []
            Q.append([i, j])
            # 단지 숫자 셀 것
            count_house = 1
            # 현재 위치도 방문 표시
            visit[i][j] = 1
            # 현재 위치도 2로 바꾸기
            matrix[i][j] = 2

            # Q가 빌때까지 돌린다
            while Q:
                # print('BFS', Q)
                state = Q.pop(0)
                x = state[0]
                y = state[1]
                for d in range(4):
                    # print(Q)
                    nx = x + dx[d]
                    ny = y + dy[d]

                    # 갈 수 있는 곳이고, 방문하지 않은 곳이면
                    if is_ok(nx, ny) == True and visit[nx][ny] == 0:
                        # Q에 넣어주기
                        Q.append([nx, ny])
                        # 방문 표시
                        visit[nx][ny] = 1
                        # matrix를 단지 숫자를 바꿔주기
                        matrix[nx][ny] = 2
                        count_house += 1

            result_list.append(count_house)

result_list.sort()
print(len(result_list))
for result in result_list:
    print(result)
