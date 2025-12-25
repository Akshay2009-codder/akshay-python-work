from collections import Counter
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        counter = Counter(nums)
        for num in counter:
            if counter[num] > 1:
                return True
        return False

print(Solution().containsDuplicate([2,14,18,22,22]))

