from Experiment import Experiment_Runner

config = {}
config['runs'] = 5
config['stats'] = ['ops', 'time']
config['algorithms'] = ["Bubble Sort", "Insertion Sort", "Quick Sort"]
config['data'] = [[5, 8, 3, 9, 0, 3, 6, 7], [5, 8, 3, 9, 0, 3, 6, 7],[5, 8, 3, 9, 0, 3, 6, 7], [5, 8, 3, 9, 0, 3, 6, 7]]


result = Experiment_Runner.run(config)

print(result)