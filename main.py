from Data import data_generator
from Experiment import Experiment_Runner
from visualization import visualizer


def run_random_data(config):
    config['data'] = [data_generator.generate_random_data(n) for n in config['sizes']]
    run_experiment(config, "Random")


def run_sorted_data(config):
    config['data'] = [data_generator.generate_sorted_data(n) for n in config['sizes']]
    run_experiment(config, "Sorted")


def run_reversed_sorted_data(config):
    config['data'] = [data_generator.generate_reversed_sorted_data(n) for n in config['sizes']]
    run_experiment(config, "Reverse Sorted")


def run_almost_sorted_data(config):
    config['data'] = [data_generator.generate_almost_sorted_data(n) for n in config['sizes']]
    run_experiment(config, "Almost Sorted")


def run_experiment(config, title):
    results = Experiment_Runner.run(config)
    visualizer.plot_result(results, title)


if __name__ == "__main__":
    config = {
        'runs': 1000,
        'stats': ['ops', 'time'],
        'algorithms': ['Bubble Sort', 'Insertion Sort', 'Quick Sort'],
        'sizes': [1, 2, 4, 8, 16, 32, 64]
    }

    run_random_data(config)
    run_sorted_data(config)
    run_reversed_sorted_data(config)
    run_almost_sorted_data(config)
