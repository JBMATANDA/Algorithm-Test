from Algorithm import BubbleSort
from Algorithm import InsertionSort
from Algorithm import QuickSort
import time


def run(config):
    results = determine_algorithm(config)

    return results


def run_algorithm(config, algorithm):
    n = config['runs']
    result_list = []
    for data in config['data']:
        ops = 0
        seconds = 0
        for _ in range(n):
            data_copy = data.copy()
            start = time.time()
            ops += algorithm.sort(data_copy)
            end = time.time()
            seconds += end - start
        results = save_results(config, data_copy, (ops / n), (seconds / n), result_list)
    return results


def save_results(config, data, count, seconds, result_list):
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


def determine_algorithm(config):
    results = {}
    for algorithm in config['algorithms']:
        if algorithm == 'Bubble Sort':
            bubble_result = run_algorithm(config, BubbleSort)
            results['Bubble Sort'] = bubble_result
        if algorithm == 'Insertion Sort':
            insertion_result = run_algorithm(config, InsertionSort)
            results['Insertion Sort'] = insertion_result
        if algorithm == 'Quick Sort':
            quick_result = run_algorithm(config, QuickSort)
            results['Quick Sort'] = quick_result
    return results
