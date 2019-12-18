N, M = map(int, input().split())

num_list = []
for i in range(N):
    num_list.append(i+1)

stop = 0

result_list = []

def make_seq(N, M):
    global result_list
    global stop

    if len(result_list) == M:
        print(" ".join(result_list))
        return

    for n in num_list:
        result_list.append(str(n))

        make_seq(N, M)

        result_list.pop()

make_seq(N, M)

