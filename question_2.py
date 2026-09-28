"""converts the list to a set, and prints the resulting set
(duplicates removed)."""
def remove_duplicates(numbers):
    return set(numbers)

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]
print(remove_duplicates(numbers))