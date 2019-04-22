import random


def generate_random_data(n):
    num_list = []
    for i in range(n):
        num_list.append(random.randrange(1, 101, 1))

    return num_list


def generate_sorted_data(n):
    num_list = generate_random_data(n)

    num_list.sort()
    return num_list


def generate_reversed_sorted_data(n):
    num_list = generate_sorted_data(n)

    num_list.reverse()
    return num_list


def generate_almost_sorted_data(n, nswap):
    num_list = generate_sorted_data(n)

    if n == 1:
        return num_list

    for i in range(nswap):
        temp = num_list[random.randrange(0, n)]
        num_list[random.randrange(0, n)] = num_list[random.randrange(0, n-1)]
        num_list[random.randrange(0, n)] = temp

    return num_list
