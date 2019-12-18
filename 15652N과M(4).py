N, M = map(int, input().split())

num_list = []
for i in range(N):
    num_list.append(i+1)

result_list = []
number = 1

def make_seq(N, M):
    global result_list
    global number

    for i in num_list:
    
        if len(result_list) == M:
            print(" ".join(result_list))
            return

        if len(result_list) == 0:
            result_list.append(str(i))
            
            make_seq(N, M)

            result_list.pop()

        else:
            if int(result_list[len(result_list)-1]) <= i:
                result_list.append(str(i))

                make_seq(N, M)

                result_list.pop()

make_seq(N, M)