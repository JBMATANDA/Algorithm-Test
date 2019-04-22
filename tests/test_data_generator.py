from Data.data_generator import generate_almost_sorted_data
from Data.data_generator import generate_random_data
from Data.data_generator import generate_reversed_sorted_data
from Data.data_generator import generate_sorted_data

n = 10
numList = [None] * n

rnumList = generate_random_data(n)
anumList = generate_almost_sorted_data(n, 4)
revnumList = generate_reversed_sorted_data(n)
snumList = generate_sorted_data(n)

print(rnumList)
print(snumList)
print(revnumList)
print(anumList)
