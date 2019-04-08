import time as time

count = 0;
def sort(a_list):
    start = time.time()
    insertion_sort(a_list)
    end = time.time()
    tid_i_sekunder = end - start
    print("Det tog %f sekunder" % tid_i_sekunder)
def insertion_sort(a_list):
        global count

        for index in range(1, len(a_list)):
            current_value = a_list[index]

            position = index

            while position > 0 and a_list[position - 1] > current_value:
                count += 1
                a_list[position] = a_list[position - 1]
                position = position - 1

            a_list[position] = current_value
