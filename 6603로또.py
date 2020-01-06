# itertools안쓰고 해보기
def perm(idx):
    

s_list = [1, 2, 3]

while s_list != []:
    s_list = list(map(int, input().split()))
    k = s_list.pop(0)
    # print(k, s_list)  //  7 [1, 2, 3, 4, 5, 6, 7]

    visit = [0] * k
    result_list = []
    idx = 0

    perm(s_list, idx)

    


    





