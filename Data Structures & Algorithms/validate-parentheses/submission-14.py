class Solution:
    def isValid(self, s: str) -> bool:
        temp = []

        for i in s:
            if i == "{" or i == "[" or i == "(":
                temp.append(i)
            else:
                if not temp: return False
                x = temp.pop()
                if i == "}" and x != "{":
                    return False
                if i == "]" and x != "[":
                    return False
                if i == ")" and x != "(":
                    return False
                

        return len(temp) == 0 

            