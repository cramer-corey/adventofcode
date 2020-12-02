from util import file_to_list
expenses = file_to_list("day_1.txt")

target = 2020
expenses_as_int = [int(expense) for expense in expenses]

for i, expense in enumerate(expenses_as_int[:-1]):
    complementary = target - expense
    if complementary in expenses[i + 1:]:
        print(expense * complementary)
        break
