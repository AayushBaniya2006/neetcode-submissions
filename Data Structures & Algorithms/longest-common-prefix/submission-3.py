class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        returnVar = ""
        temp = ""

        for i in range(len(strs[0])):
            for x in range(1, len(strs),1):
                if(i >= len(strs[x]) or strs[0][i] != strs[x][i]):
                    return returnVar
            returnVar += strs[0][i]

        return returnVar