board = []
check = []
num = 0
bingo = 0


for b in range(5):
    b_list = list(map(int, input().split()))
    board.append(b_list)

for c in range(5):
    c_list = list(map(int, input().split()))
    check.extend(c_list)
num = 0
flag = 1
while num < 25
    for i in range(5):
        cnt = 0
        for j in range(5):
            # 불려진 숫자 체크
            if board[i][j] == check[num]:
                board[i][j] = 0
            num += 1
            print(board)
            # for row in range(5):
            #     # 대각선검사
            #     if board[row][row] == 0:
            #         cnt += 1
            #         if cnt == 5:
            #             result = num + 1
            #             break
            #
            #     if board[4-row][row] == 0:
            #         cnt += 1
            #     if cnt == 5:
            #         result = num + 1
            #         break
            #
            #     for col in range(5):
            #         # 가로검사
            #         if board[row][col] == 0:
            #             cnt += 1
            #             if cnt == 5:
            #                 bingo += 1
            #         if bingo == 3:
            #             result = num + 1
            #             break
            #
            #         # 세로검사
            #         if board[row][col] == 0:
            #             cnt += 1
            #             if cnt == 5:
            #                 bingo += 1
            #         if bingo == 3:
            #             result = num + 1
            #             break
            #