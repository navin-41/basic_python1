def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage:
nums = [1, 2, 4, 5, 6]
missing_number = find_missing_number(nums)
print("The missing number is:", missing_number) 