class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        if len(s) == 1:
            return False
        
        for x in s:
            if x == '[' or x == '(' or x == '{':
                temp.append(x)
            else:
                if(len(temp) == 0):
                    return False
                elif x == ']' and temp[-1] != '[':
                    return False
                elif x == '}' and temp[-1] != '{':
                    return False
                elif x == ')' and temp[-1] != '(':
                    return False
                else:
                    temp.pop()
        return len(temp) == 0
