'''
3 7
4 0 0 0 0 0 0
0 0 0 2 0 0 0
0 0 0 0 0 0 4

답 = 0
'''

def printmat(matrix):
    for n in range(N):
        print(matrix[n])

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

num_dir = [0, 4, 2, 4, 4, 1]

# matrix를 돌면서 숫자 순서대로 저장 -> 숫자와 대응하는 direct_list작성
num_list = []
# 숫자가 상응하는 direct_list -> 모든 방향combination list작성
direct_list = []
# 숫자들의 idx 저장하는 idx_list -> 여기서부터 감시가능범위 시작
idx_list = []
# 모든 방향조합이 들어갈 list
combination_list = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0:
            num_list.append(matrix[i][j])
            idx_list.append((i, j))

for num in num_list:
    direct_list.append(num_dir[num])

# print(direct_list)  =  [4, 2, 4]
# print(idx_list)  =  [(0, 0), (1, 3), (2, 6)]

# 방향 4, 2, 4를 424로만들기
direct_num = ''
for n in direct_list:
    direct_num += str(n)
direct_num = int(direct_num)

for nn in range(111, direct_num+1):
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

print(combination_list)
    



