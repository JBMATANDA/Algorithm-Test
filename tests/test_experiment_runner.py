from Experiment import Experiment_Runner
from Algorithm import BubbleSort
from Data import data_generator

config = {
    'runs': 5,
    'stats': ['ops', 'time'],
    'algorithms': ["Bubble Sort", "Insertion Sort", "Quick Sort"],
    'data': [[5, 8, 3, 9, 0, 3, 6, 7], [5, 8, 3, 9, 0, 3, 6, 7], [5, 8, 3, 9, 0, 3, 6, 7], [5, 8, 3, 9, 0, 3, 6, 7]]
}

result = Experiment_Runner.run(config)
seconds, ops = Experiment_Runner.run_algorithm(config, data_generator.generate_random_data(100), algorithm=BubbleSort)

print(seconds)
print(ops)
print(result)
