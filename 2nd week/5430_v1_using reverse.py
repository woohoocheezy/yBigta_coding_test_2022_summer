from sys import stdin

# reverse 반복하니깐 시간 초과

def FuncD():

    global only_num_list
    # print("in funcD : ", only_num_list)

    # if only_num_list is None:
    if len(only_num_list) == 0 :
        return 0
    else :
        only_num_list = only_num_list[1:]
        print(only_num_list)
        return 1 

def FuncR():
    global only_num_list
    # if only_num_list is None:
    # print("in funR : ", only_num_list)
    if len(only_num_list) != 0 :
        # only_num_list = only_num_list.reverse() # doesn't work
        only_num_list.reverse()


T = int(stdin.readline())

for i in range(T):

    p = stdin.readline().rstrip()


    n = int(stdin.readline())

    num_list = stdin.readline().rstrip()


    only_num_list = num_list[1:-1].split(",")

    if n == 0 :
        only_num_list.pop()

    print(only_num_list, type(p))
    for func in p :
        if func == "R":
            FuncR()
        else : # "D"
            output = FuncD()

            if output == 0 :
                print("error")
                break
    else: # join으로 연습
        print("[",end="")
        for i, out_num in enumerate(only_num_list):
            if i != len(only_num_list)-1:
                print(f"{out_num},",end="")
            else:
                print(f"{out_num}]")
        



