class Solution:
    def lengthOfLastWord(self, s: str) -> int:
     words = s.strip().split(" ")
     if words:
         last = words[-1]
         last_len = len(last)
     return last_len
     return last
print(Solution().lengthOfLastWord("Akshay dhumda"))

