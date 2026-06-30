class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = {}

        if(len(s) != len(t)):
            return False
        

        for i in range(len(s)):
            if s[i] not in temp:
                temp[s[i]] = 0
            if t[i] not in temp:
                temp[t[i]] = 0
            
            temp[s[i]] = temp[s[i]] + 1
            temp[t[i]] = temp[t[i]] - 1

        for i in temp:
            if(temp[i] != 0):
                return False
            

        return True