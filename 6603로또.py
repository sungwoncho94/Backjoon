# itertools안쓰고 해보기
def perm():
    global max_num

    if len(result_list) == 6:
        print(" ".join(map(str, result_list)))
        return

    for idx in range(k):
        if visit[idx] == 0 and s_list[idx] > max_num:
            result_list.append(s_list[idx])
            max_num = s_list[idx]
            visit[idx] = 1
            # print("1", result_list)
            perm()

            visit[idx] = 0
            result_list.pop()
            max_num = 0

s_list = [1, 2, 3]

while s_list != []:
    s_list = list(map(int, input().split()))
    k = s_list.pop(0)
    # print(k, s_list)  //  7 [1, 2, 3, 4, 5, 6, 7]

    visit = [0] * k
    result_list = []
    idx = 0
    max_num = 0

    perm()
    print()
