

def sort(a_list):
    global count
    count = 0
    insertion_sort(a_list)
    return count


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]

        position = index

        while increment_count() and position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


def increment_count():
    global count
    count += 1
    return True
