""" Convert valid entries to integers (ignore invalid values).
    2. Keep only numbers greater than 10.
    3. Square each of the remaining numbers.
    4. Compute the sum of those squares."""
def calculate_sum(nums):
    numbers=[]
    for num in nums:
        try:
            numbers.append(int(num))
        except ValueError:
            pass
    result=[num**2 for num in numbers if num >10]
    return sum(result)
nums = ["10", "20", "abc", "30", "5"]
print(calculate_sum(nums))