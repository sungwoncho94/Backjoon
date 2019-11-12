import copy
'''
3 7
4 0 0 0 0 0 0
0 0 0 2 0 0 0
0 0 0 0 0 0 4

답 = 0
'''
# 해야할것
# 문제! 가지치기는 어떻게 할 것인가??
# 함수 안으로 넣어서 while문 돌리고, matrix에서 0개수 찾기
# 초기화는 어떻게 시켜줄것인가?


# CCTV마다, 방향별로 똑같은 코드를 계속 반복해서 쓰는 문제가 있다 ==> 일정 방향으로 진행하는 함수를 만들어서 코드를 간소화시키자


def in_range(x, y):
    # in_range == True이면 계속 시행, False가 되는 순간 끝난다
    if 0 <= x < N and 0 <= y < M and matrix[x][y] != 6:
        return True
    return False

def printmat(matrix):
    for n in range(N):
        print(matrix[n])
    print('--------------------')

def right(x, y):
    global matrix
    global change
    while in_range(x, y):
        y += 1
        # 0일때만 감시지역으로 바꾸고, CCTV일때는 그냥 지나간다
        if matrix[x][y] == 0:
            matrix[x][y] = '#'
        change += 1

def left(x, y):
    global matrix
    global change
    while in_range(x, y):
        y -= 1
        # 0일때만 감시지역으로 바꾸고, CCTV일때는 그냥 지나간다
        if matrix[x][y] == 0:
            matrix[x][y] = '#'
        change += 1

def up(x, y):
    global matrix
    global change
    while in_range(x, y):
        x -= 1
        # 0일때만 감시지역으로 바꾸고, CCTV일때는 그냥 지나간다
        if matrix[x][y] == 0:
            matrix[x][y] = '#'
        change += 1

def down(x, y):
    global matrix
    global change
    while in_range(x, y):
        x += 1
        # 0일때만 감시지역으로 바꾸고, CCTV일때는 그냥 지나간다
        if matrix[x][y] == 0:
            matrix[x][y] = '#'
        change += 1

# 그냥 처음부터 다시 생각해서 풀자


# CCTV and direct 함수 설정
def find_BS(x, y):
    global matrix
    global change
    if CCTV_num == 1:


    elif CCTV_num == 2:
        
    elif CCTV_num == 3:
        

    elif CCTV_num == 4:
        print("4로 들어옴")
        x1 = x2 = x3 = x
        y1 = y2 = y3 = y
        print(x1, x2, x3)

        # 왼, 위, 오
        if direct_num == 1:

            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3):
                x1 -= 1
                if in_range(x1, y1) and matrix[x1][y1] == 0:
                    matrix[x1][y1] = "#"
                    change += 1

                y2 -= 1
                if in_range(x2, y2) and matrix[x2][y2] == 0:
                    matrix[x2][y2] = "#"
                    change += 1
                
                y3 += 1    
                if in_range(x3, y3) and matrix[x3][y3] == 0:
                    matrix[x3][y3] = "#"
                    change += 1
                   
                printmat(matrix)

        # 위, 오, 아
        elif direct_num == 2:
            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3):
                x1 -= 1
                if in_range(x1, y1) and matrix[x1][y1] == 0:
                    matrix[x1][y1] = "#"
                    change += 1

                x2 += 1
                if in_range(x2, y2) and matrix[x2][y2] == 0:
                    matrix[x2][y2] = "#"
                    change += 1

                y3 += 1
                if in_range(x3, y3) and matrix[x3][y3] == 0:
                    matrix[x3][y3] = "#"
                    change += 1


        # 오, 아, 왼
        elif direct_num == 3:
            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3):
                y1 += 1
                if in_range(x3, y3) and matrix[x3][y3] == 0:
                    matrix[x1][y1] = "#"
                    change += 1

                x2 += 1
                if in_range(x2, y2) and matrix[x2][y2] == 0:
                    matrix[x2][y2] = "#"
                    change += 1

                y3 -= 1
                if matrix[x3][y3] == 0:
                    matrix[x3][y3] = "#"
                    change += 1

        # 아, 왼, 위
        elif direct_num == 4:
            while in_range(x1, y1) or in_range(x2, y2) or in_range(x3, y3):
                x1 -= 1
                if in_range(x1, y1) and matrix[x1][y1] == 0:
                    matrix[x1][y1] = "#"
                    change += 1

                y2 -= 1
                if in_range(x2, y2) and matrix[x2][y2] == 0:
                    matrix[x2][y2] = "#"
                    change += 1

                x3 += 1
                if in_range(x3, y3) and matrix[x3][y3] == 0:
                    matrix[x3][y3] = "#"
                    change += 1


N, M = map(int, input().split())
# 실제로 바꿀 matrix
matrix = [list(map(int, input().split())) for _ in range(N)]
# 초기화용 matrix
origin_matrix = copy.deepcopy(matrix)

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

max_change = 0


# combination을 돌면서 순서대로 최소 사각지대 구하기
for comb in combination_list:  # [4, 2, 4] 방향설정
    change = 0
    # CCTV하나하나마다(방향 하나하나마다) CCTV감시구역 표시
    for i in range(len(CCTV_list)):  # 4  /  2  /  4
        # CCTV 번호 설정
        CCTV_num = CCTV_list[i]
        # 방향 설정
        direct_num = comb[i]
        # 현재 idx설정  ->  (x, y)자체가 find_BS함수로 넘어갈 수 있도록 바꾸자
        (x, y) = idx_list[i]
        find_BS(x, y)
        if max_change < change:
            max_change = change
    # comb 하나 다 돌았으면 matrix 초기화
    matrix = copy.deepcopy(origin_matrix)
    

zero_cnt = 0
for i in range(N):
    for i in range(M):
        if origin_matrix[i][j] == 0:
            zero_cnt += 1
result = zero_cnt - max_change

print(result)


