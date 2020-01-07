# 방법1 - 숫자를 선택함 / 하지않음 의 방식으로 구하면 2**n으로 구할 수 있다 -> 시간복잡도가 많이 줄어든다
# 2진수 사용 or &연산 사용 or 재귀 사용 (ㅇ)
# 방법2 - itertools - combinations 사용해서 조합 구한 후, 오름차순으로 정렬

# 방법 1 

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
            max_num = i
            visit[i] = 1
            combination(N, M)
            visit[i] = 0
            result.pop()
            max_num = 0

combination(N, M)