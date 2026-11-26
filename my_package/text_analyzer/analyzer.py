from collections import Counter
import matplotlib.pyplot as plt


def sum_counters(*counters):
    """Sum multiple Counter objects."""
    return sum(counters, Counter())


def plot_counter_most_common(top_items):
    """Plot the most common items."""
    words = [item[0] for item in top_items]
    counts = [item[1] for item in top_items]

    plt.bar(words, counts)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Most Common Words")
    plt.show()


def plot_counter(counter, n_most_common=5):
    """Plot the most common items from a Counter."""
    top_items = counter.most_common(n_most_common)
    plot_counter_most_common(top_items)