N, M = map(int, input().split())
# N = 숫자 개수
# M = 수열 길이 수 


# visit이 있는 DFS처럼 풀어보자!!!
number_list = []
visit = [0] * (N+1)
result = []
s_list = []
for i in range(1, N+1):
    number_list.append(i)

def sequence(N, M):
    if len(s_list) == M:
        for a in range(M):
            print(s_list[a], end=' ')
        print()
        return
    else: 
        for i in range(1, N+1):
            if visit[i] == 0:
                visit[i] = 1
                s_list.append(i)
                sequence(N, M)
                s_list.pop()
                visit[i] = 0

sequence(N, M)

