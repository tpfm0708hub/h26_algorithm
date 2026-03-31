num_list = [23, 45, 27, 11, 25, 65, 78]

def getindex(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target: 
            result = num_list.index(target)
    return result

def getMax(num_list):
    max_num = 0        

    for i in num_list:
        if i > max_num: max_num
    return i
    
def getMin(num_list):
    min_num = num_list[0]

    for i in num_list:
        if min_num < i: min_num
    return min_num
    
def countGT(num_list, target):
    cnt_01 = 0
    for i in num_list:
        if target < i : cnt_01 += 1
    return cnt_01

def sumList(num_list):
    sum_01 = 0
    for i in num_list:
        sum_01 += i
    return sum_01

def swapList(num_list):
    list_01 = []

    for i in range(len(num_list)-1,-1,-1):
        list_01.append(num_list[i])
    return list_01
   
print(getindex(num_list, 25))
print(getMax(num_list))
print(getMin(num_list))
print(countGT(num_list, 42))
print(sumList(num_list))
num_list = swapList(num_list)
print(num_list)