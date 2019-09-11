import copy

N = int(input())

result = []  # i가 바뀔때마다 값을 넣어놓자
dice_list = []

for n in range(N):
    dice_list.append(list(map(int, input().split())))


i = 0
while i < 6:  # 첫번째 주사위의 바닥 숫자를 0~5 idx까지 돌아가며 선택
    d = 0  # dice idx

    # 시작 바닥숫자가 바뀔때마다 다른 값을 구해야하니까 새롭게 list만들어서 시작
    test_list = []
    test_list = copy.deepcopy(dice_list)

    # (1) 1번 주사위의 바닥, 위 idx와 번호 구하기

    if i == 0:
        bottom = test_list[d][i]  # d = 0, i = 0 --> 1번째 주사위의 1번 idx값
        top = test_list[d][5]  # A-F == 0-5
    elif i == 1 or i == 2:
        bottom = test_list[d][i]
        top = test_list[d][i+2]
    elif i == 3 or i == 4:
        bottom = test_list[d][i]
        top = test_list[d][i-2]
    elif i == 5:
        bottom = test_list[d][i]
        top = test_list[d][0]

    # (2) 1번 주사위에서 bottom, top 삭제
    test_list[d].remove(bottom)
    test_list[d].remove(top)

    d += 1  # 다음 주사위로 넘어감
    
    # (3) 1번주사위 top == 2번 주사위bottom 인 idx구하기
    # 2번 주사위의 bottom_idx, top_idx가 정해짐
    while d <= N - 1:
        bottom_idx = test_list[d].index(top)
        if bottom_idx == 0:
            top_idx = 5
        elif bottom_idx == 1 or bottom_idx == 2:
            top_idx = bottom_idx + 2
        elif bottom_idx == 3 or bottom_idx == 4:
            top_idx = bottom_idx - 2
        elif bottom_idx == 5:
            top_idx = 0
        bottom = test_list[d][bottom_idx]
        top = test_list[d][top_idx]

        test_list[d].remove(test_list[d][bottom_idx])
        test_list[d].remove(top)

        d += 1 

    # i = 0 -> test_list = [[3, 1, 6, 5], [3, 2, 6, 5], [5, 4, 3, 2], [1, 3, 2, 5], [1, 6, 5, 2]]
    temp_result = 0
    for a in range(N):
        temp_result += max(test_list[a])
    result.append(temp_result)
    i += 1

print(max(result))

'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3
'''