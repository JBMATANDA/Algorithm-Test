from Algorithm import BubbleSort
from Algorithm import InsertionSort
from Algorithm import QuickSort
import time



def run(config):
    result = {}

    #Runs every Algorthim in config
    for i in config['algorithms']:
        #Bubble Sort
        if i == 'Bubble Sort':
            resultList = []
            for j in config['data']:
                count = 0
                seconds = 0
                for k in (range(config['runs'])):
                    data = j.copy()
                    #Starts timer
                    start = time.time()
                    count += BubbleSort.sort(data)
                    end = time.time()
                    seconds += float(end - start)
                    seconds = round(seconds, 2)

                #Adds operations and time
                if config['stats'] == ['ops', 'time']:
                    resultList.append({'n': len(j), 'ops': count / config['runs'], 'time': seconds / config['runs']})
                #Adds operations
                if config['stats'] == 'ops':
                    resultList.append({'n': len(j), 'ops': count / config['runs']})
                #Adds time
                if config['stats'] == 'time':
                    resultList.append({'n': len(j), 'time': seconds / config['runs']})
            #Saves result in map
            result['Bubble Sort'] = resultList
        #Insertion Sort
        if i == 'Insertion Sort':
            resultList = []
            for j in config['data']:
                count = 0
                seconds = 0
                for k in (range(config['runs'])):
                    data = j.copy()
                    #Starts timer
                    start = time.time()
                    count += InsertionSort.sort(data)
                    end = time.time()
                    seconds += float(end - start)
                    seconds = round(seconds, 2)
                # Adds operations and time
                if config['stats'] == ['ops', 'time']:
                    resultList.append({'n': len(j), 'ops': count / config['runs'], 'time': seconds / config['runs']})
                # Adds operations
                if config['stats'] == 'ops':
                    resultList.append({'n': len(j), 'ops': count / config['runs']})
                # Adds time
                if config['stats'] == 'time':
                    resultList.append({'n': len(j), 'time': seconds / config['runs']})
            # Saves result in map
            result['Insertion Sort'] = resultList
        #Quick Sort
        if i == 'Quick Sort':
            resultList = []
            for j in config['data']:
                count = 0
                seconds = 0
                for k in (range(config['runs'])):
                    data = j.copy()
                    # Starts timer
                    start = time.time()
                    count += QuickSort.sort(data)
                    end = time.time()
                    seconds += float(end - start)
                    seconds = round(seconds, 2)
                # Adds operations and time
                if config['stats'] == ['ops', 'time']:
                    resultList.append({'n': len(j), 'ops': count / config['runs'], 'time': seconds / config['runs']})
                # Adds operations
                if config['stats'] == 'ops':
                    resultList.append({'n': len(j), 'ops': count / config['runs']})
                # Adds time
                if config['stats'] == 'time':
                    resultList.append({'n': len(j), 'time': seconds / config['runs']})
            # Saves result in map
            result['Quick Sort'] = resultList

    return result


def run_algorithm(config, data, algorithm):
    ops = 0
    seconds = 0
    for runs in range(config['runs']):
        start = time.time()
        ops += algorithm.sort(data)
        end = time.time()
        seconds += end - start

    return seconds / float(config['runs']), ops / float(config['runs'])
