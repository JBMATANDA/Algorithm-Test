from Test.AlmostSorted import generate_almost_sorted_data
from Test.RandomData import generate_random_data
from Test.ReveresedSortedData import generate_reversed_sorted_data
from Test.SortedData import generate_sorted_data
from Algorithm.BubbleSort import bubble_sort
from Algorithm.InsertionSort import insertion_sort
from Algorithm.QuickSort import quick_sort
size = 10

sortedList = generate_sorted_data(size)
almsortList = generate_almost_sorted_data(size)
revsortedList = generate_reversed_sorted_data(size)
randList = generate_random_data(size)

def run(numlist,algList):

