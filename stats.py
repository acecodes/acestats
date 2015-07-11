"""
Some code borrowed from Data Science From Scratch (Grus)
"""
import matplotlib.pyplot as plt
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
    sample_distribution = [1, 5, 29, 321, 12, 125, 99, 72]
    print(Stats.mean(sample_distribution))
    print(Stats.median(sample_distribution))
