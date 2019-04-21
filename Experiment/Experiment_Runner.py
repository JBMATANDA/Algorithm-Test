from Algorithm import BubbleSort
from Algorithm import InsertionSort
from Algorithm import QuickSort
import time


def run(config):
    result = {}

    # Runs every Algorithm in config
    for i in config['algorithms']:
        # Bubble Sort
        if i == 'Bubble Sort':
            for j in config['data']:
                for _ in (range(config['runs'])):
                    count, seconds = run_algorithm(config, j, BubbleSort)
                result_list = save_results(config, j, count, seconds)
            # Saves result in map
            result['Bubble Sort'] = result_list
        # Insertion Sort
        if i == 'Insertion Sort':
            for j in config['data']:
                for _ in (range(config['runs'])):
                    count, seconds = run_algorithm(config, j, InsertionSort)
                result_list = save_results(config, j, count, seconds)
            # Saves result in map
            result['Insertion Sort'] = result_list
        # Quick Sort
        if i == 'Quick Sort':
            for j in config['data']:
                count, seconds = run_algorithm(config, j, QuickSort)
            result_list = save_results(config, j, count, seconds)
            # Saves result in map
            result['Quick Sort'] = result_list

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


def save_results(config, data, count, seconds):
    result_list = []
    # Adds operations and time
    if config['stats'] == ['ops', 'time']:
        result_list.append({'n': len(data), 'ops': count, 'time': seconds})
    # Adds operations
    if config['stats'] == 'ops':
        result_list.append({'n': len(data), 'ops': count})
    # Adds time
    if config['stats'] == 'time':
        result_list.append({'n': len(data), 'time': seconds})
    return result_list
