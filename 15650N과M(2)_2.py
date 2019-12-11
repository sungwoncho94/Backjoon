N, M = map(int, input().split())

visit = [0] * (N+1)
max_num = 0
result = []

def combination(N, M):
    global max_num
    # range(N) -> 0~N-1  //  내가 원하는 것은 n ~ N-1 idx까지 들어가는 것
    if sum(visit) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N+1):
        if visit[i] == 0 and i > max_num:
            result.append(i)
            if i > max_num:
                max_num = i
            visit[i] = 1
            combination(N, M)
            visit[i] = 0
            result.pop()
            max_num = 0

combination(N, M)