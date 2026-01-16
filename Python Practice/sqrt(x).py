import math

class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = math.sqrt(x)
        return  int(sqrt)

print(Solution().mySqrt(8))