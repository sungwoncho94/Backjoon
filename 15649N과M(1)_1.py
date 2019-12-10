from itertools import permutations

N, M = map(int, input().split())

num_list = []
for n in range(N):
    num_list.append(n+1)

perm_list = permutations(num_list, M)

for perm in perm_list:
    print(" ".join(map(str, perm)))