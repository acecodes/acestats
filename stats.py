"""
Some code borrowed from Data Science From Scratch (Grus)
"""
import matplotlib.pyplot as plt
from collections import Counter

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
