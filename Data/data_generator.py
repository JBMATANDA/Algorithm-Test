import random


def generate_random_data(n):
    numList = []
    for i in range(n):
        numList.append(random.randrange(1, 101, 1))

    return numList

def generate_sorted_data(n):
    numList = []
    for i in range(n):
        numList.append(random.randrange(1, 101))

    numList.sort()
    return numList

def generate_reversed_sorted_data(n):
    numList = []
    for i in range(n):
        numList.append(random.randrange(1, 101, 1))

    numList.sort(reverse=True)
    return numList

def generate_almost_sorted_data(n):
    numList = []
    for i in range(n):
        numList.append(random.randrange(1, 101, 1))
        numList.sort()


    for i in range(2):
        temp = numList[i]
        numList[i] = numList[random.randrange(0, n)]
        numList[random.randrange(0, n)] = temp

    return numList
