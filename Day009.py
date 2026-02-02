"""
Write a function that calculates and returns the mean of provided numeric data.
It should handle a simple list like [2, 3, 4] or a list of tuples like [(1, 2), (3, 5)],
where the first element is the value and the second is the frequency.
"""

# def mean(numbers):
#     total = sum(numbers)
#     no_of_items = len(numbers)
#     average = total/no_of_items
#     print(f"The mean for given list of numbers is {average}")

# mean([1, 2, 3, 4, 5])


def calculate_median(user_list):
    sorted_list = sorted(user_list)
    N = len(sorted_list)
    if N % 2 != 0:
        median_index = (N + 1) // 2
        median = sorted_list[median_index - 1]
        return median
    else:
        initial_index = (N // 2) - 1
        final_index = N // 2
        median = (sorted_list[initial_index] + sorted_list[final_index]) / 2
        return median


med = calculate_median([4, 5, 6, 7, 8])
print(med)

"""
Write a function that returns the median of data provided in a list.
"""

"""
Write a function that returns the mode of data provided in both forms described above
(simple list and value-frequency tuples).
"""

"""
Write a function that returns the variance and standard deviation of data given in a list.
"""

"""
Write a function that calculates the covariance and Pearson correlation between two data samples,
re-using the above functions.
"""
