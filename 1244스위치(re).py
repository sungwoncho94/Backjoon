switch = int(input())
s_list = list(map(int, input().split()))
s_list.insert(0, 9)  # 가장 앞에 의미없는 값인 9를 삽입하여 idx맞춰주기
s_list.append(9)
people = int(input())

for p in range(people):
    gender, card_num = map(int, input().split())  # 사람 한명씩 와서 스위치할 것  # [1, 3]

    if gender == 1:  # 남자면
        i = 1
        while card_num * i < switch + 1:
            if s_list[card_num * i] == 1:
                s_list[card_num * i] = 0
            elif s_list[card_num * i] == 0:
                s_list[card_num * i] = 1
            i += 1
        # print(s_list)

if gender == 2:  # 여자면 뽑은 카드부터 바꿔
    if s_list[card_num] == 1:
        s_list[card_num] = 0
    elif s_list[card_num] == 0:
        s_list[card_num] = 1
    i = 1  # i = 1부터 시작
    # card_num기준 양쪽이 같다면
    while s_list[card_num - i] == s_list[card_num + i]:
        # card_num +- i가 범위 내에 있다면,
        # print(card_num -i, card_num + i)
        # card_num -1 바꾸기
        if s_list[card_num - i] == 1:
            s_list[card_num - i] = 0
        elif s_list[card_num - i] == 0:
            s_list[card_num - i] = 1
        # card_num + 1 바꾸기
        if s_list[card_num + i] == 1:
            s_list[card_num + i] = 0
        elif s_list[card_num + i] == 0:
            s_list[card_num + i] = 1
        # i 값 1 올려서 반복
        i += 1
        if card_num - i >= 1 and card_num + i < switch + 1:
            continue
        else:
            break
        
        # print(s_list)

s_list.pop(0)
s_list.pop()
# prt = 0
# for s in s_list:
#     print(s, end=" ")
#     prt += 1
#     if prt == 20:
#         prt = 0
#         print()

for s in range(len(s_list)):
    print(s_list[s], end=' ')
    if (s + 1) % 20 == 0:
        print('')

'''
39
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
2
1 2
2 3
[1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0]
[0 1 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0]

40
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
2
1 2
2 20
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
'''

