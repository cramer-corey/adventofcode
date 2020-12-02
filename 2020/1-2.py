from itertools import combinations

from day_1_data import *

target = 2020


def findTriplets(expenses, target):
    def valid(val):
        return sum(val) == target

    return list(filter(valid, list(combinations(expenses, 3))))


matching_expenses = findTriplets(expenses, target)
print(matching_expenses[0][0] * matching_expenses[0][1] *
      matching_expenses[0][2])
