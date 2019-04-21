import time as time

def sort(a_list):
    count = insertion_sort(a_list)
    return count

def insertion_sort(a_list, count = 0):
    for index in range(1, len(a_list)):
        current_value = a_list[index]

        position = index

        while position > 0 and a_list[position - 1] > current_value:
            count = count + 1
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    return count