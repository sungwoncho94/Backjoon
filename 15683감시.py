import itertools
'''
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
# 20

6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
# 15

6 6
1 0 0 0 0 0
0 1 0 0 0 0
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 0 1 0
0 0 0 0 0 1
# 6
'''

def printmat(matrix):
    for a in range(len(matrix)):
        print(matrix[a])


'''
def R, L, U, D
다른 CCTV(1~5)는 건너뛸 수 있다
0 -> #로 바꾸면서 나아간다
벽(6)은 지나갈 수 없다
'''
# def right(CCTV, direction):
    

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
CCTV_list = []
dir_list = [4, 2, 4, 4, 1]

for n in range(N):
    for m in range(M):
        if 1 <= matrix[n][m] < 6:
            CCTV_list.append(matrix[n][m])

'''
1. CCTV종류에 따라 가능한 방향 combination 만들기
2. combination을 방향으로 받으며, CCTV종류와 방향을 받는 find(CCTV, 방향) 함수 만들기
3. CCTV와 방향에 따라 어떻게 이동해야하는지 설정
    - right, left, up, down 함수 만들어줘서 CCTV종류와 방향에 맞게 움직일 수 있도록 해주기
'''



