N = int(input())
max_len = 0
max_num = 0
len_list = []

for n in range(1, N+1):  # 1부터 N-1까지 돌아가면서 2번째 수를 정한다.
    num_list = []
    num_list.append(N)
    num_list.append(n)

    for i in range(N+1):  # 음수가 나오기 전까지만 num_list를 구함
        a = num_list[i] - num_list[i+1]
        if a < 0:
            break
        num_list.append(a)
    length = len(num_list)

    # print(num_list)

    if length >= max_len:
        max_len = length  # n이 진행될때마다 max_len 구하기
        max_num = n  # max_len이 나올 때 max_num 구해놓기

result = []
result.append(N)
result.append(max_num)
for i in range(N+1):  # 음수가 나오기 전까지만 num_list를 구함
    a = result[i] - result[i + 1]
    if a < 0:
        break
    result.append(a)

print(max_len)
for k in result:
    print(k, end=' ')