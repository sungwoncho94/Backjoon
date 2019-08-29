# 가로 2, 3  /  세로 4

N, M = map(int, input().split())
matrix = [['0'] * N for i in range(M)]
cut = int(input())
num_list = []
cnt_list = []

for c in range(cut):
    num, idx = map(int, input().split())
    if num == 0:
        for i in range(idx):
            for j in range(N):
                matrix[i][j] += 'a'
        for i in range(idx, M):
            for j in range(N):
                matrix[i][j] += 'b'

    elif num == 1:
        for i in range(M):
            for j in range(idx):
                matrix[i][j] += 'c'
        for i in range(M):
            for j in range(idx, N):
                matrix[i][j] += 'd'

for i in range(M):
    for j in range(N):
        if matrix[i][j] not in num_list:
            num_list.append(matrix[i][j])
# num_list = [12, 13, 14, 15]

cnt = 0
for n in num_list:
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == n:
                cnt += 1
    cnt_list.append(cnt)
    cnt = 0
    
# cnt_list = [8, 16, 26, 30]
# print(matrix)
# print(num_list)
# print(cnt_list)
print(max(cnt_list))



'''
for c in range(cut):
    num, idx = map(int, input().split())
    M_list.append(idx) if num == 0 else N_list.append(idx)
M_list.insert(0, 0)
M_list.append(M)
N_list.insert(0, 0)
N_list.append(N)

# print(M_list)  # [0, 3, 2]
# print(N_list)  # [0, 4]
i = j = 0
while i < len(M_list) and j < len(N_list):
    for a in range(M_list[i], M_list[i+1]):
        for b in range(N_list[j], N_list[j+1]):
            matrix[a][b] = c
        j += 1

        c += 1
    i += 1

print(matrix)
'''
# for i in range(2):
#     for j in range(4):
#         matrix[i][j] = 1

# for i in range(2):
#     for j in range(4, N):
#         matrix[i][j] = 2

# for i in range(2, 3):
#     for j in range(4):
#         matrix[i][j] = 3

# for i in range(2, 3):
#     for j in range(4, N):
#         matrix[i][j] = 4

# for i in range(3, M):
#     for j in range(4):
#         matrix[i][j] = 5

# for i in range(3, M):
#     for j in range(4, N):
#         matrix[i][j] = 6


# print(matrix)

