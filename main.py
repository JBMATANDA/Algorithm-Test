from Data import data_generator
from Experiment import Experiment_Runner
from visualization import visualizer


if __name__ == "__main__":
    config = {}
    config['runs'] = 100
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

    config['data'] = [data_generator.generate_sorted_data(1),
                      data_generator.generate_sorted_data(2),
                      data_generator.generate_sorted_data(4),
                      data_generator.generate_sorted_data(8),
                      data_generator.generate_sorted_data(16),
                      data_generator.generate_sorted_data(32),
                      data_generator.generate_sorted_data(64)]

    results = Experiment_Runner.run(config)
    visualizer.plot_result(results, "Sorted")

    config['data'] = [data_generator.generate_reversed_sorted_data(1),
                      data_generator.generate_reversed_sorted_data(2),
                      data_generator.generate_reversed_sorted_data(4),
                      data_generator.generate_reversed_sorted_data(8),
                      data_generator.generate_reversed_sorted_data(16),
                      data_generator.generate_reversed_sorted_data(32),
                      data_generator.generate_reversed_sorted_data(64)]

    results = Experiment_Runner.run(config)
    visualizer.plot_result(results, "Reverse Sorted")

    config['data'] = [data_generator.generate_almost_sorted_data(1),
                      data_generator.generate_almost_sorted_data(2),
                      data_generator.generate_almost_sorted_data(4),
                      data_generator.generate_almost_sorted_data(8),
                      data_generator.generate_almost_sorted_data(16),
                      data_generator.generate_almost_sorted_data(32),
                      data_generator.generate_almost_sorted_data(64)]

    results = Experiment_Runner.run(config)
    visualizer.plot_result(results, "Almost Sorted")
