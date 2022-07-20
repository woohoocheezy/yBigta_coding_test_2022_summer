from collections import deque
from sys import stdin

def FuncD():
    global only_num_list

    if len(only_num_list) == 0 :
        return 0

    else :
        if r_counter % 2 == 0:
            only_num_list.popleft()
        else :
            only_num_list.pop()
            
        return 1 

def FuncR():
    global r_counter
    r_counter += 1


T = int(stdin.readline())

for i in range(T):

    p = stdin.readline().rstrip()


    n = int(stdin.readline())

    num_list = stdin.readline().rstrip()

    r_counter = 0

    only_num_list = deque(num_list[1:-1].split(","))

    if n == 0 :
        only_num_list.pop()

    for func in p :
        if func == "R":
            FuncR()
        else : # "D"
            output = FuncD()

            if output == 0 :
                print("error")
                break
    else:
        if r_counter % 2 == 1:
            only_num_list.reverse()

        print("[",end="")
        for i, out_num in enumerate(only_num_list):
            if i != len(only_num_list)-1:
                print(f"{out_num},",end="")
            else:
                print(f"{out_num}",end="")
        print("]")
        