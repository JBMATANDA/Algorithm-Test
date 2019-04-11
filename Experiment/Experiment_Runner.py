from Data import data_generator
from Algorithm import BubbleSort
from Algorithm import InsertionSort
from Algorithm import QuickSort
import time

config = {}
config['runs'] = 1
config['stats'] = ['ops', 'time']
config['algorithms'] = ["Bubble Sort", "Insertion Sort", "Quick Sort"]
config['data'] = [data_generator.generate_random_data(1000),
                  data_generator.generate_sorted_data(1000),
                  data_generator.generate_reversed_sorted_data(1000),
                  data_generator.generate_almost_sorted_data(1000)]


def run(config):
    result = {}

    #Runs every Algorthim in config
    for i in config['algorithms']:
        #Bubble Sort
        if i == 'Bubble Sort':
            resultList = []
            for j in config['data']:
                count = 0
                data = j.copy()
                for k in range(config['runs']):
                    #Starts timer
                    start = time.time()
                    count += BubbleSort.sort(data)
                    end = time.time()
                    seconds = float(end - start)
                    seconds = round(seconds, 2)
                #Adds operations and time
                if config['stats'] == ['ops', 'time']:
                    resultList.append({'ops': count / config['runs'], 'time': seconds})
                #Adds operations
                if config['stats'] == 'ops':
                    resultList.append({'ops': count / config['runs']})
                #Adds time
                if config['stats'] == 'time':
                    resultList.append({'time': seconds})
            #Saves result in map
            result['Bubble Sort'] = resultList
        #Insertion Sort
        if i == 'Insertion Sort':
            resultList = []
            for j in config['data']:
                count = 0
                data = j.copy()
                for k in range(config['runs']):
                    #Starts timer
                    start = time.time()
                    count += InsertionSort.sort(data)
                    end = time.time()
                    seconds = float(end - start)
                    seconds = round(seconds, 2)
                # Adds operations and time
                if config['stats'] == ['ops', 'time']:
                    resultList.append({'ops': count / config['runs'], 'time': seconds})
                # Adds operations
                if config['stats'] == 'ops':
                    resultList.append({'ops': count / config['runs']})
                # Adds time
                if config['stats'] == 'time':
                    resultList.append({'time': seconds})
            # Saves result in map
            result['Insertion Sort'] = resultList
        #Quick Sort
        if i == 'Quick Sort':
            resultList = []
            for j in config['data']:
                count = 0
                data = j.copy()
                for k in range(config['runs']):
                    # Starts timer
                    start = time.time()
                    count += QuickSort.sort(data)
                    end = time.time()
                    seconds = float(end - start)
                    seconds = round(seconds, 2)
                # Adds operations and time
                if config['stats'] == ['ops', 'time']:
                    resultList.append({'ops': count / config['runs'], 'time': seconds})
                # Adds operations
                if config['stats'] == 'ops':
                    resultList.append({'ops': count / config['runs']})
                # Adds time
                if config['stats'] == 'time':
                    resultList.append({'time': seconds})
            # Saves result in map
            result['Quick Sort'] = resultList

    return result

run(config)