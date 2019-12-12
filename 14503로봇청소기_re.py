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

ax = [0, -1, 0, 1]
ay = [-1, 0, 1, 0]

bx = [1, 0, -1, 0]
by = [0, -1, 0, 1]

next_dir = [3, 0, 1, 2]

def cleaning(x, y, d):
    global cleaned_room, matrix, flag, dir_check

    while flag == 1:
        # (1) 일단청소
        if matrix[x][y] == 0:
            matrix[x][y] = 8
            cleaned_room += 1

        # (2) 사방 탐색
        x += ax[d]
        y += ay[d]
        # 내가 가려는 곳이 청소 가능한 곳일 때만 이동함
        if 0 <= x < N and 0 <= y < M and matrix[x][y] == 0:
            d = next_dir[d]  # 회전 (이미 좌표는 옮겨져 있음)            
            dir_check = [0, 0, 0, 0]
            continue
        else:  # 내가 가려는 곳이 갈 수 없는 곳이라면
            x -= ax[d]  # 다시 제자리로 좌표 돌려놓기
            y -= ay[d]
            dir_check[d] = 1
            d = next_dir[d]  # 회전은 시켜야함
        
        # (3) 사방이 모두 벽이거나, 청소가 되어있는 겨우 -> 후진여부만 살펴보기
        if sum(dir_check) == 4:
            # 이미 후진시켜놓음
            x += bx[d]
            y += by[d]

            if matrix[x][y] == 1:
                flag = 0
            # 후진할 수 있는 경우
            else:
                dir_check = [0, 0, 0, 0]
                

cleaning(x, y, d)
print(cleaned_room)