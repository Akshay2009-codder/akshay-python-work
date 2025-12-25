from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single_digit = []
        count = Counter(nums)
        for num in count:
            if count[num] == 1:
                single_digit.append(num)
        return single_digit

print(Solution().singleNumber([2,2,1]))
