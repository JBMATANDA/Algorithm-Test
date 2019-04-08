from Test.AlmostSorted import generate_almost_sorted_data
from Test.RandomData import generate_random_data
from Test.ReveresedSortedData import generate_reversed_sorted_data
from Test.SortedData import generate_sorted_data
from Algorithm.BubbleSort import bubble_sort

n = 10
numList = [None] * n

rnumList = generate_random_data(n)
anumList = generate_almost_sorted_data(n)
revnumList = generate_reversed_sorted_data(n)
snumList = generate_sorted_data(n)

if __name__ == '__main__':
    print("Before: " % rnumList)
    bubble_sort(rnumList)
    print("After: " % rnumList)
