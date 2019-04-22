from Experiment import Experiment_Runner

config = {
    'runs': 5,
    'stats': ['ops', 'time'],
    'algorithms': ["Bubble Sort", "Insertion Sort", "Quick Sort"],
    'data': [[5, 8, 3, 9, 0, 3, 6, 7]]
}

result = Experiment_Runner.run(config)

print(result)
