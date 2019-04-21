import time as time

def sort(a_list):
    count = bubble_sort(a_list)
    return count

def bubble_sort(a_list, count = 0):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            count = count + 1
            if a_list[i] > a_list[i + 1]:

                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    return count
