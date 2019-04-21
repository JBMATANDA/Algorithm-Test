

def sort(a_list):
    global count
    count = 0
    bubble_sort(a_list)
    return count


def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if increment_count() and a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


def increment_count():
    global count
    count += 1
    return True
