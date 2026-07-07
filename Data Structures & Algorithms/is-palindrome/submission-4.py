class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            while l < r and not self.isValid(s[l]):
                l += 1
            while r > l and not self.isValid(s[r]):
                r -= 1
            else:
                if(s[l].lower() != s[r].lower()):
                    return False
                l += 1
                r -= 1
        return True
                
        

    def isValid(self, pos):
        return (ord('A') <= ord(pos) <= ord('Z') 
        or ord('a') <= ord(pos) <= ord('z')  
        or ord('0') <= ord(pos) <= ord('9'))
