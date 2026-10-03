class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        temp = {}
        tempT = {}

        for i in range(len(s)):
            temp[s[i]] = temp.get(s[i], 0) + 1 
            tempT[t[i]] = tempT.get(t[i], 0) + 1 

        return temp == tempT
            
            
