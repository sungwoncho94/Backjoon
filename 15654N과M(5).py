N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list.sort()

result_list = []

visit_list = [0] * (N)

def make_seq(N, M):
    if len(result_list) == M:
        print(" ".join(result_list))
        return

    for n in range(len(N_list)):
        if visit_list[n] == 0:
            result_list.append(str(N_list[n]))
            visit_list[n] = 1

            make_seq(N, M)

            result_list.pop()
            visit_list[n] = 0

make_seq(N, M)

# N_list에서 M개의 수를 고를 후, 수열을 만든다
# 수열은 오름차순
# 1 7 / 7 1 가능

'''
4 2
9 8 7 1

1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8
'''





