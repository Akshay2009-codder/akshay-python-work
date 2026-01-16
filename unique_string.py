class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = []
        current = ""
        for ch in s:
            if ch in current:
                unique.append(current)
                current = ""
            current += ch
        if current:
            unique.append(current)

        length = 0
        for substring in unique:
            if len(substring) > length:
                length = len(substring)
        return length

print(Solution().lengthOfLongestSubstring("dvdf"))

