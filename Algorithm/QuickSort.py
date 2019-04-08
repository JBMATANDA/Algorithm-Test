import time as time

def sort(a_list):
    start = time.time()
    quick_sort(a_list)
    end = time.time()
    tid_i_sekunder = end - start
    print("Det tog %f sekunder" % tid_i_sekunder)

def quick_sort(a_list):
    start = time.time()
    quick_sort_helper(a_list, 0, len(a_list) - 1)
    end = time.time()
    tid_i_sekunder = end - start
    print("Det tog %f sekunder" % (tid_i_sekunder))

def quick_sort_helper(a_list, first, last):
    if first < last:

        split_point = partition(a_list, first, last)

        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)


def partition(a_list, first, last):
    pivot_value = a_list[first]

    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and \
                      a_list[left_mark] <= pivot_value:
              left_mark = left_mark + 1

          while a_list[right_mark] >= pivot_value and \
                     right_mark >= left_mark: