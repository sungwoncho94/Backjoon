N = int(input())
matrix = []
for n in range(N):
    n_list = list(map(int, input().split()))
    matrix.append(n_list)

    ishouse = 1  # 1 이상이면 집임. 숫자는 단지번호에 따라 커질 것.

    # 단지 번호는 2부터 시작하기 (처음 나오는 집도 2로 만들기)
    danji = 2

    # 시작점을 잡고 오른쪽탐색, 되돌아와서 왼쪽 탐색, 모두 끝나면 i + 1

    # 시작 idx 찾기  (가장 위, 가장 왼쪽 -> j는 계속 바뀜)
    flag = 1
    for i in range(N):
        if flag == 0:
            break
        for j in range(N):
            if matrix[i][j] > 0:
                start_i = i
                start_j = j
                flag = 0
                break

    # 오른쪽탐색
    while matrix[]

    temp_i = start_i
    temp_j = start_j
    while matrix[temp_i][temp_j + 1] == 1:
        matrix[temp_i][temp_j + 1] = danji
        if end_j <= temp_j:
            end_j = temp_j

    while matrix[start_i + 1][end_j] == 1:
        end_i = start_i + 1



    for i in range(start_i, end_i + 1):
