class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        l, r = 0, 0 
        ret = 0 
        while r < len(s):
            while s[r] in temp: 
                    temp.remove(s[l])
                    l += 1
            ret = max(ret, r-l + 1)
            temp.add(s[r])
            r+=1
        return ret 