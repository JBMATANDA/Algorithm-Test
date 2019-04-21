import random


def generate_random_data(n):
    num_list = []
    for i in range(n):
        num_list.append(random.randrange(1, 101, 1))

    return num_list


def generate_sorted_data(n):
    num_list = []
    for i in range(n):
        num_list.append(random.randrange(1, 101))

    num_list.sort()
    return num_list


def generate_reversed_sorted_data(n):
    num_list = []
    for i in range(n):
        num_list.append(random.randrange(1, 101, 1))

    num_list.sort(reverse=True)
    return num_list


def generate_almost_sorted_data(n):

    num_list = []
    for i in range(n):
        num_list.append(random.randrange(1, 101, 1))
        num_list.sort()

    if n == 1:
        return num_list

    for i in range(2):
        temp = num_list[i - 1]
        num_list[i] = num_list[random.randrange(0, n)]
        num_list[random.randrange(0, n)] = temp

    return num_list
