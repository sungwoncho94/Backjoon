# # 방법1 - 숫자를 선택함 / 하지않음 의 방식으로 구하면 2**n으로 구할 수 있다 -> 시간복잡도가 많이 줄어든다
# # 2진수 사용 or &연산 사용 or 재귀 사용 (ㅇ)
# # 방법2 - itertools - combinations 사용해서 조합 구한 후, 오름차순으로 정렬

# # 방법 1 ------ 오답
# N, M = map(int, input().split())

# visit = [0] * (N+1)
# max_num = 0
# result = []

# def combination(N, M):
#     global max_num
#     # M개의 숫자를 골랐으면 멈춘 후, print해준다
#     if sum(visit) == M:
#         print(" ".join(map(str, result)))
#         return
#     # visit = N+1개 list
#     for i in range(1, N+1):
#         # i 에 visit한 적이 없고, i가 max_num보다 클 때에만 다음 숫자로 선택한다.
#         if visit[i] == 0 and i > max_num:
#             result.append(i)
#             # max_num을 현재 선택한 숫자로 바꿔준다
#             if i > max_num:
#                 max_num = i
#             # visit표시해주기
#             visit[i] = 1
#             # 재귀 돌기
#             combination(N, M)
#             # 재귀가 끝난 후, 원상태로 돌려주기 (visit, result_list, max_num)
#             visit[i] = 0
#             result.pop()
#         max_num = 0

# combination(N, M)

# # -----------------답

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