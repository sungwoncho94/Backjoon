data = [1, 2, 3, 4]
visit = [False] * (len(data) + 1)
result = []
N = int(input())
# arr는 data에서 가능한 list중 하나 ex. [1], [2, 3]과 같음
# 순열 (4P3)
def permutation(arr):
    if len(arr) == N:  # 만약 data갯수만큼 하나하나 1~4개까지 하고싶다면, for문 돌리기!
        result.append(arr)
        return result
    else:
        for idx in range(len(data)):
            if visit[idx]:
                continue
            elif visit[idx] == False:
                visit[idx] = True
                permutation(arr + [data[idx]])
                visit[idx] = False  # 전 단계의 visit만 초기화

permutation([])
print(result)


# # 조합(4C3)
# #  굳이 visit 필요 없음  why? 어차피 k + 1번째값부터 다시 보기 때문!
def combination(arr, k):
    if len(arr) == N:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(data)):  # 순서 없음 -> 전 값보다 큰 것만 나와야함
            combination(arr + [data[idx]], idx)

combination([], -1)  # -1을 넣어야 인덱스 0(첫번째 값)부터 돌면서 확인
print(result)


# 중복순열
def d_permutation(arr):
   if len(arr) == N:
       result.append(arr)
       return result
   else:
       for idx in range(len(data)):
           d_permutation(arr + [data[idx]])
d_permutation([])
print(result)