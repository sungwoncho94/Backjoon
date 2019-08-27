def find_count(M, S):
    for i in range(len(S)):
        total_count = 0
        for j in range(5):
            for k in range(5):
                if M[j][k] == S[i]:
                    M[j][k] = 0

        d1_sum = 0
        d2_sum = 0
        for j in range(5):
            d1_sum += M[j][j]
            d2_sum += M[j][4 - j]
            sero_sum = 0
            if sum(M[j]) == 0:
                total_count += 1

            for k in range(5):
                sero_sum += M[k][j]
            if sero_sum == 0:
                total_count += 1

        if d1_sum == 0:
            total_count += 1
        if d2_sum == 0:
            total_count += 1

        if total_count >= 3:
            return i + 1


M = [list(map(int, input().split())) for i in range(5)]  # 내 빙고판
S = []
for i in range(5):
    S.extend(list(map(int, input().split())))  # 사회자가 부르는 번호

print(find_count(M, S))