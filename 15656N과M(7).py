N, M = map(int, input().split())
N_list = list(map(int, input().split()))

result_list = []

def solve(N, M):
    for i in range(N):
        if len(result_list) == M:
            if result_list not in check_list:
                print(result_list)
            return
        result_list.append(n)
d
