import matplotlib
import math
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plot_result(results, title):
    plt.suptitle(title)
    plt.ylabel('Ops (#)')
    plt.xlabel('Size (n)')

    bubble_opsx, bubble_opsy, bubble_timey = bubble_sort_stats(results)
    insertion_opsx, insertion_opsy, insertion_timey = insertion_sort_stats(results)
    quick_opsx, quick_opsy, quick_timey = quick_sort_stats(results)

    plt.subplot(121)
    plt.plot(bubble_opsx, bubble_opsy, label='Bubble Sort')
    plt.plot(insertion_opsx, insertion_opsy, label='Insertion Sort')
    plt.plot(quick_opsx, quick_opsy, label='Quick Sort')
    plt.plot(quick_opsx, constant(quick_opsx), label='Constant', linestyle='--')
    plt.plot(quick_opsx, logarithmic(quick_opsx), label='Logarithmic', linestyle='--')
    plt.plot(quick_opsx, linear(quick_opsx), label='Linear', linestyle='--')
    plt.plot(quick_opsx, quadratic(quick_opsx), label='Quadratic', linestyle='--')

    plt.legend(loc='upper left')
    plt.title("Ops")

    plt.subplot(122)
    plt.plot(bubble_opsx, bubble_timey, label='Bubble Sort')
    plt.plot(insertion_opsx, insertion_timey, label='Insertion Sort')
    plt.plot(quick_opsx, quick_timey, label='Quick Sort')
    plt.title("Time")
    plt.legend(loc='upper left')

    plt.show()


def logarithmic(n):
    return [math.log2(i) for i in n]


def constant(n):
    return [1 for _ in n]


def quadratic(n):
    return [float(i) ** 2 for i in n]


def linear(n):
    return n


def bubble_sort_stats(results):
    bubble_sort = results['Bubble Sort']

    bubble_opsx = []
    bubble_opsy = []
    bubble_timey = []

    for stat in bubble_sort:
        bubble_opsx.append(stat['n'])
        bubble_opsy.append(stat['ops'])
        bubble_timey.append(stat['time'])

    return bubble_opsx, bubble_opsy, bubble_timey


def insertion_sort_stats(results):
    insertion_sort = results['Insertion Sort']

    insertion_opsx = []
    insertion_opsy = []
    insertion_timey = []

    for stat in insertion_sort:
        insertion_opsx.append(stat['n'])
        insertion_opsy.append(stat['ops'])
        insertion_timey.append(stat['time'])

    return insertion_opsx, insertion_opsy, insertion_timey


def quick_sort_stats(results):
    quick_sort = results['Quick Sort']

    quick_opsx = []
    quick_opsy = []
    quick_timey = []

    for stat in quick_sort:
        quick_opsx.append(stat['n'])
        quick_opsy.append(stat['ops'])
        quick_timey.append(stat['time'])

    return quick_opsx, quick_opsy, quick_timey
