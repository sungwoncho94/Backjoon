N, M = map(int, input().split())

visit_list = [0] * N
# 정답 숫자들이 들어갈 list
perm_list = []
# 재귀함수 안에서 global 로 사용할 정답 리스트
result_list = []

def permutation(N, M):
    if sum(visit_list) == M:
        print(" ".join(map(str, result_list)))
        return result_list
    for i in range(N):
        if visit_list[i] == 0:  # 해당 번호에 방문한적이 없으면
            result_list.append(i+1)  # 그 숫자를 result_list에 넣어준다
            visit_list[i] = 1
            permutation(N, M)
            visit_list[i] = 0
            result_list.pop()


permutation(N, M)
