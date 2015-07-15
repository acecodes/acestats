"""
Some code borrowed from Data Science From Scratch (Grus)
"""
import matplotlib.pyplot as plt
import math
from collections import Counter


class Stats:
    """
    Commonly used statistical methods
    All functions are staticmethods
    """

    @staticmethod
    def mean(distribution):
        """
        Average (mean) of a distribution
        """
        return sum(distribution) / len(distribution)

    @staticmethod
    def median(distribution):
        """Find the middle value of a distribtion (v)"""
        n = len(distribution)
        sorted_distribution = sorted(distribution)
        midpoint = n // 2

        if n % 2 == 1:
            return sorted_distribution[midpoint]

        else:
            low = midpoint - 1
            high = midpoint
            return (sorted_distribution[low] + sorted_distribution[high]) / 2

    @staticmethod
    def quantile(distribution, p):
        """Return the pth-percentile value in distribution"""
        p_index = int(p * len(distribution))
        return sorted(distribution)[p_index]

    @staticmethod
    def mode(distribution):
        """Return most common value(s) in distribution"""
        counts = Counter(distribution)
        max_count = max(counts.values())
        return [x_i for x_i, count in counts.iteritems() if count == max_count]

    @staticmethod
    def data_range(distribution):
        """Return range of distribution"""
        return max(distribution) - min(distribution)

    @staticmethod
    def de_mean(distribution):
        """Translate distribution by subtracting its mean (mean == 0)"""
        x_bar = Stats.mean(distribution)
        return [x_i - x_bar for x_i in distribution]

    @staticmethod
    def variance(distribution):
        """Calculates the variance of a distribution"""

        n = len(distribution)
        deviations = Stats.de_mean(distribution)
        return Vector.sum_of_squares(deviations) / (n-1)

    @staticmethod
    def standard_deviation(distribution):
        """Standard deviation of a distribution"""
        return math.sqrt(Stats.variance(distribution))

    @staticmethod
    def interquartile_range(distribution):
        """Handles outliers better"""
        return Stats.quantile(distribution, 0.75) - Stats.quantile(distribution, 0.25)

    @staticmethod
    def covariance(variable1, variable2):
        """Measures how two variables vary in tandem from their means"""
        n = len(variable1)
        return Vector.dot_product(Stats.de_mean(variable1), Stats.de_mean(variable2) / (n - 1))

    @staticmethod
    def correlation(variable1, variable2):
        """Check correlation between two variables"""
        stdev_1 = Stats.standard_deviation(variable1)
        stdev_2 = Stats.standard_deviation(variable2)
        if stdev_1 > 0 and stdev_2 > 0:
            return Stats.covariance(variable1, variable2) / stdev_1 / stdev_2
        else:
            return 0  # If there isn't any variation, correlation is zero


class Vector:
    """
    Vector operations
    Borrowed from my linear algebra repo
    """

    @staticmethod
    def dot_product(v, w):
        """Sum of componentwise products"""
        return (sum(v_i * w_i for v_i, w_i in zip(v, w)))

    @staticmethod
    def sum_of_squares(v):
        """v_1 * v_1 + ... v_n * v_n"""
        return Vector.dot_product(v, v)


def friends_histogram():
    """Display a frequency distribution within a histogram"""
    num_friends = [100, 50, 23, 99, 85, 87, 34, 45]

    friend_counts = Counter(num_friends)
    xs = range(101)
    ys = [friend_counts[x] for x in xs]

    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title('Friend Counts Histogram')
    plt.xlabel('# of friends')
    plt.ylabel('# of people')
    plt.show()

if __name__ == '__main__':
    sample_distribution = [92, 5, 29, 200, 5, 12, 125, 99, 72, 2]
    print('Sample distribution: {}'.format(sample_distribution))
    print('Mean: {}'.format(Stats.mean(sample_distribution)))
    print('Median: {}'.format(Stats.median(sample_distribution)))
    print('Mode: {}'.format(Stats.mode(sample_distribution)))
    print('Quantile: {}'.format(Stats.quantile(sample_distribution, 0.2)))
    print('Range: {}'.format(Stats.data_range(sample_distribution)))
    print('Standard deviation: {}'.format(Stats.standard_deviation(sample_distribution)))
    print('Interquartile range: {}'.format(Stats.interquartile_range(sample_distribution)))
