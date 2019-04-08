from Data import data_generator


rnumList = data_generator.generate_random_data(10)
snumList = data_generator.generate_sorted_data(10)
revnumList = data_generator.generate_reversed_sorted_data(10)
anumList = data_generator.generate_almost_sorted_data(10)

algList = ["Bubble Sort", "Insertion Sort", "Quick Sort"]
dataList = [rnumList, snumList, revnumList, anumList]

nsort = 2

def run(algList, dataList, nsort, stat):


    print(dataList, algList, nsort, stat)