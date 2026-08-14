def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]
        
        seen.update({nums[i] : i})
    return []

assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
