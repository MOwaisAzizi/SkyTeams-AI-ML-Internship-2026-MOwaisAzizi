from collections import Counter
import text_analyzer

counter1 = Counter(["AI", "Python", "AI", "ML"])
counter2 = Counter(["Python", "AI", "Data", "ML"])

word_count_totals = text_analyzer.sum_counters(
    counter1, counter2
)

print(word_count_totals)

text_analyzer.plot_counter(word_count_totals)