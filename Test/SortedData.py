import random
numList = []

def generate_sorted_data(n):
    for i in range(n):
        numList.append(random.randrange(1,101,1))

    numList.sort()
    return numList



