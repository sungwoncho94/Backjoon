melon = int(input())

dir_list = []
len_list = []

for i in range(6):
    num_list = list(map(int, input().split()))
    dir_list.append(num_list[0])
    len_list.append(num_list[1])

s12 = s34 = o12 = o34 = 0
# 값 하나짜리 긴 길이의 곱 - 작은 사각형의 곱
#(1) 먼저 곱해줄 큰 변의 길이 = s12, s34 구하기  s12 = 2  /  s34 = 4
if dir_list.count(1) == 1:
    s12 = 1
    o12 = 2
else:
    s12 = 2
    o12 = 1

if dir_list.count(3) == 1:
    s34 = 3
    o34 = 4
else:
    s34 = 4
    o34 = 3

# o12, o34의 idx구하기  (242 / 424 / 131 / 313 처럼 사이에 끼어있어야함)
len_s12 = len_s34 = len_o12 = len_o34 = 0

# len_s12, len_s34구하기
len_s12 = len_list[dir_list.index(s12)]
len_s34 = len_list[dir_list.index(s34)]

# o12의 길이 구하기
for i in range(6):
    if i == 0:
        if dir_list[5] == o34 and dir_list[1] == o34:
            len_o12 = len_list[0]
    elif i == 5:
        if dir_list[4] == o34 and dir_list[0] == o34:
            len_o12 = len_list[5]
    else:
        if dir_list[i-1] == o34 and dir_list[i+1] == o34:
            len_o12 = len_list[i]

# o34의 길이 구하기
for i in range(6):
    if i == 0:
        if dir_list[5] == o12 and dir_list[1] == o12:
            len_o34 = len_list[0]
    elif i == 5:
        if dir_list[4] == o12 and dir_list[0] == o12:
            len_o34 = len_list[5]
    else:
        if dir_list[i-1] == o12 and dir_list[i+1] == o12:
            len_o34 = len_list[i]

# 결과 구하기
result = (len_s12 * len_s34 - len_o12 * len_o34) * melon

print(result)

