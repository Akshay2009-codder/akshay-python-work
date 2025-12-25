class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for str in strs:
            for s in strs[1:]:
                while not s.startswith(prefix):
                    prefix =  prefix[:-1]
                    if prefix == "":
                        return ""

        return prefix
print(Solution().longestCommonPrefix(["flower","flow","flight"]))

