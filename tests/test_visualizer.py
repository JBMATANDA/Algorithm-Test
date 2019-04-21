from Data import data_generator
from Experiment import Experiment_Runner
from visualization import visualizer


config = {}
config['runs'] = 5
config['stats'] = ['ops', 'time']
config['algorithms'] = ['Bubble Sort', 'Insertion Sort', 'Quick Sort']
config['data'] = [data_generator.generate_random_data(1),
                  data_generator.generate_random_data(2),
                  data_generator.generate_random_data(4),
                  data_generator.generate_random_data(8),
                  data_generator.generate_random_data(16),
                  data_generator.generate_random_data(32),
                  data_generator.generate_random_data(64)]


results = Experiment_Runner.run(config)
visualizer.plot_result(results, "Random")
