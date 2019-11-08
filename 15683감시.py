'''
3 7
4 0 0 0 0 0 0
0 0 0 2 0 0 0
0 0 0 0 0 0 4

답 = 0
'''
# 해야할것
# 문제! 가지치기는 어떻게 할 것인가??
# 함수 안으로 넣어서 while문 돌리고, matrix에서 0값 찾기
# 초기화는 어떻게 시켜줄것인가?


def in_range(x, y):
    # in_range == True이면 계속 시행, False가 되는 순간 끝난다
    if 0 <= x < N and 0 <= y < M and matrix[x][y] != 6:
        return True
    return False

def printmat(matrix):
    for n in range(N):
        print(matrix[n])

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

num_dir = [0, 4, 2, 4, 4, 1]

# matrix를 돌면서 숫자 순서대로 저장 -> 숫자와 대응하는 direct_list작성
CCTV_list = []
# 숫자가 상응하는 direct_list -> 모든 방향combination list작성
direct_list = []
# 숫자들의 idx 저장하는 idx_list -> 여기서부터 감시가능범위 시작
idx_list = []
# 모든 방향조합이 들어갈 list
combination_list = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            CCTV_list.append(matrix[i][j])
            idx_list.append((i, j))

for num in CCTV_list:
    direct_list.append(num_dir[num])

# print(direct_list)  =  [4, 2, 4]
# print(idx_list)  =  [(0, 0), (1, 3), (2, 6)]

# 방향 4, 2, 4를 424로만들기
d_num = ''
for n in direct_list:
    d_num += str(n)
d_num = int(d_num)

for nn in range(111, d_num+1):
    sn_list = []
    is_zero = False
    str_nn = str(nn)
    for s in str_nn:
        if s == '0':
            is_zero = True
    if is_zero == False:
        for s in str_nn:
            sn_list.append(int(s))
        combination_list.append(sn_list)


for comb in combination_list:
    for i in range(len(CCTV_list)):
        # CCTV 번호 설정
        CCTV_num = CCTV_list[i]
        # 방향 설정
        direct_num = comb[i]
        # 현재 idx설정  ->  (x, y)자체가 find_BS함수로 넘어갈 수 있도록 바꾸자
        (x, y) = idx_list[i]


# CCTV and direct 함수 설정
def find_BS(x, y):
    if CCTV_num == 1:
        # 오른쪽으로 전진
        if direct_num == 1:
            while in_range(x, y):
                if matrix[x][y] == 0:
                    # '#'이면 세기 힘드니까 -1로 바꿔준 후, 0만 세자
                    matrix[x][y] = -1
                    y += 1

        # 아래로 전진
        elif direct_num == 2:
            while in_range(x, y):
                if matrix[x][y] == 0:
                    # '#'이면 세기 힘드니까 -1로 바꿔준 후, 0만 세자
                    matrix[x][y] = -1
                    x += 1

        # 왼쪽으로 전진
        elif direct_num == 3:
            while in_range(x, y):
                if matrix[x][y] == 0:
                    # '#'이면 세기 힘드니까 -1로 바꿔준 후, 0만 세자
                    matrix[x][y] = -1
                    y -= 1

        # 위로 전진
        elif direct_num == 4:
            while in_range(x, y):
                if matrix[x][y] == 0:
                    # '#'이면 세기 힘드니까 -1로 바꿔준 후, 0만 세자
                    matrix[x][y] = -1
                    x -= 1

    elif CCTV_num == 2:
        x1 = x2 = x
        y1 = y2 = y
        # 오/왼으로 가기
        if direct_num == 1:
            # 둘 다 범위에 없을때 끝내기 (하나라도 범위에 있으면 계속돌려)
            while in_range(x1, y1) or in_range(x2, y2):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    y += 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    y -= 1
        # 위/아래로 가기
        elif direct_num == 2:
            while in_range(x1, y1) or in_range(x2, y2):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    x += 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    x -= 1


    elif CCTV_num == 3:
        x1 = x2 = x
        y1 = y2 = y
        # 위/오른쪽
        if direct_num == 1:
            while in_range(x1, y1) or in_range(x2, y2):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    x -= 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    y += 1

        # 오른쪽/아래
        elif direct_num == 2:
            while in_range(x1, y1) or in_range(x2, y2):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    y += 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    x += 1

        # 아래/왼쪽
        elif direct_num == 3:
            while in_range(x1, y1) or in_range(x2, y2):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    x += 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    y -= 1

        # 왼쪽/위
        elif direct_num == 4:
            while in_range(x1, y1) or in_range(x2, y2):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    x -= 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    y -= 1

    elif CCTV_num == 4:
        x1 = x2 = x3 = x
        y1 = y2 = y3 = y

        # 왼, 위, 오
        if direct_num == 1:
            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    x -= 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    y -= 1
                if matrix[x3][y3] == 0:
                    matrix[x3][y3] = -1
                    y += 1

        # 위, 오, 아
        elif direct_num == 2:
            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    x -= 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    x += 1
                if matrix[x3][y3] == 0:
                    matrix[x3][y3] = -1
                    y += 1

        # 오, 아, 왼
        elif direct_num == 3:
            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    y += 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    x += 1
                if matrix[x3][y3] == 0:
                    matrix[x3][y3] = -1
                    y -= 1
        # 아, 왼, 위
        elif direct_num == 4:
            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    x -= 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    y -= 1
                if matrix[x3][y3] == 0:
                    matrix[x3][y3] = -1
                    x += 1

    # 사방탐색
    elif CCTV_num == 5:
        x1 = x2 = x3 = x4 = x
        y1 = y2 = y3 = y4 = y
            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3) or in_range(x4, y4):
                if matrix[x1][y1] == 0:
                    matrix[x1][y1] = -1
                    x -= 1
                if matrix[x2][y2] == 0:
                    matrix[x2][y2] = -1
                    y -= 1
                if matrix[x3][y3] == 0:
                    matrix[x3][y3] = -1
                    x += 1
                if matrix[x4][y4] == 0:
                    matrix[x4][y4] = -1
                    y += 1

