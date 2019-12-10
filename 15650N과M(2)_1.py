from itertools import combinations
# 방법1 - 숫자를 선택함 / 하지않음 의 방식으로 구하면 2**n으로 구할 수 있다 -> 시간복잡도가 많이 줄어든다
# 방법2 - itertools - combinations 사용해서 조합 구한 후, 오름차순으로 정렬
# 방법3 - itertools - permutations 사용해서 순열 구한 후, 오름차순으로 정렬하여 result_list 에 넣어둔 후, 비교를 통해 없을 때만 출력 -> 비효율

# 방법 2
N, M = map(int, input().split())

num_list = []

for n in range(N):
    num_list.append(n+1)

comb_list = combinations(num_list, M)

for comb in comb_list:
    result_list = []
    for c in comb:
        result_list.append(str(c))

    print(" ".join(result_list))

