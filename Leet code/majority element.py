from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = Counter(nums)
        n = len(nums)
        for num in counter:
            if counter[num] > n // 2:
                return num
print(Solution().majorityElement([3,2,3]))
