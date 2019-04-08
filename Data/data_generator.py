import random

numList = []

def generate_random_data(n):
    for i in range(n):
        numList.append(random.randrange(1,101,1))

    print (list)

def generate_sorted_data(n):
    for i in range(n):
        numList.append(random.randrange(1,101,1))

    numList.sort()
    return numList

def generate_reversed_sorted_data(n):
    for i in range(n):
        numList.append(random.randrange(1, 101, 1))

    numList.sort(reverse=True)
    return numList

def generate_almost_sorted_data(n):
    for i in range(n):
        numList.append(random.randrange(1, 101, 1))
        numList.sort()

    for i in range(n / 2):
        temp = numList[i]
        numList[i] = numList[i + 1]
        numList[i + 1] = temp

        return numList