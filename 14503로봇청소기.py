def print_mat(matrix):
    for i in range(N):
        print(matrix[i])    
    
N, M = map(int, input().split())
# x = 북으로부터 떨어짐  /  y = 서쪽으로부터 떨어짐  /  0:북, 1:동, 2:남, 3:서
x, y, d = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(N)]

cleaned_room = 0

flag = 1
dir_check = [0, 0, 0, 0]

# matrix 내에 있을 때, 주변이 청소가능한지 4방향을 모두 확인
def check_left(x, y):
    if 0 <= x < N and 0 <= y-1 < M:
        if matrix[x][y-1] == 0:
            return True

def check_up(x, y):
    if 0 <= x-1 < N and 0 <= y < M:
        if matrix[x-1][y] == 0:
            return True

def check_right(x, y):
    if 0 <= x < N and 0 <= y+1 < M:
        if matrix[x][y+1] == 0:
            return True

def check_down(x, y):
    if 0 <= x+1 < N and 0 <= y < M:
        if matrix[x+1][y] == 0:
            return True

def cleaning(x, y, d):
    global cleaned_room, matrix, flag, dir_check

    while flag == 1:
        if matrix[x][y] == 0:
            matrix[x][y] = 8
            cleaned_room += 1

        # 현재 방향에서 왼쪽으로 돌면서 청소가능 여부 살펴보기
        if d == 0:  # 위/북쪽
            if check_left(x, y) == True:
                d = 3  # 왼쪽으로 회전
                y = y-1  # 왼쪽으로 한칸이동
                dir_check = [0, 0, 0, 0]
                continue
            else:
                d = 3
                # 왼쪽으로 이동할 수 없는 경우(=d_0에서 움직일 수 없는 경우)
                dir_check[0] = 1
                # sum != 4 -> 아직 4방향을 다 보지 않았음 -> 다시 위에서부터 방향에 맞게 돌아야함
                # sum == 4가 된다면 4방향이 다 불가하다는 뜻임
                if sum(dir_check) != 4:
                    continue
        elif d == 1:  # 우/동쪽
            if check_up(x, y) == True:
                d = 0  # 위쪽으로 회전
                x = x-1  # 위쪽으로 한칸이동
                dir_check = [0, 0, 0, 0]
                continue
            else:
                d = 0
                dir_check[1] = 1
                if sum(dir_check) != 4:
                    continue
        elif d == 2:  # 하/남쪽
            if check_right(x, y) == True:
                d = 1  
                y = y+1
                dir_check = [0, 0, 0, 0]
                continue
            else:
                d = 1
                dir_check[2] = 1
                if sum(dir_check) != 4:
                    continue
        else:  # 좌/서쪽
            if check_down(x, y) == True:
                d = 2  
                x = x+1
                dir_check = [0, 0, 0, 0]
                continue
            else:
                d = 2
                dir_check[3] = 1
                if sum(dir_check) != 4:
                    continue

        # 사방이 모두 벽이거나, 청소가 되어있는 경우 -> 후진여부만 살펴보기
        if sum(dir_check) == 4:
            # 이미 사방이 모두 벽이거나 청소가 되어있는 상황. 뒤가 벽이면 종료하고, 벽이 아니라면 후진한 뒤, dir_check 초기화
            if d == 0:
                if matrix[x+1][y] == 1:
                    flag = 0
                # 벽이 아니라서 후진할 수 있는 경우,
                else:
                    x = x+1
                    dir_check = [0, 0, 0, 0]
                    continue
            elif d == 1:
                # 뒤가 벽이라서 후진 못하는 경우 -> 끝
                if matrix[x][y-1] == 1:
                    flag = 0
                # 벽이 아니라서 후진할 수 있는 경우,
                else:
                    y = y-1
                    dir_check = [0, 0, 0, 0]
                    continue
            elif d == 2:
                # 뒤가 벽이라서 후진 못하는 경우 -> 끝
                if matrix[x-1][y] == 1:
                    flag = 0
                # 벽이 아니라서 후진할 수 있는 경우,
                else:
                    x = x-1
                    dir_check = [0, 0, 0, 0]
                    continue
            else:
                # 뒤가 벽이라서 후진 못하는 경우 -> 끝
                if matrix[x][y+1] == 1:
                    flag = 0
                # 벽이 아니라서 후진할 수 있는 경우,
                else:
                    y = y+1
                    dir_check = [0, 0, 0, 0]
                    continue

cleaning(x, y, d)
print(cleaned_room)