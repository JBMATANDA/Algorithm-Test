import time as time

def sort(a_list):
    count = quick_sort(a_list)
    return count

def quick_sort(a_list, count = 0):
    return quick_sort_helper(a_list, 0, len(a_list) - 1, count)



def quick_sort_helper(a_list, first, last, count):
    if first < last:

        split_point, count = partition(a_list, first, last, count)
        count = quick_sort_helper(a_list, first, split_point - 1, count)
        count = quick_sort_helper(a_list, split_point + 1, last, count)
    return count


def partition(a_list, first, last, count):
    pivot_value = a_list[first]
    count += 1

    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and \
                      a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while a_list[right_mark] >= pivot_value and \
            right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
        temp = a_list[first]
        a_list[first] = a_list[right_mark]
        a_list[right_mark] = temp


        return right_mark, count



