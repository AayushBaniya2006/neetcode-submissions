class Solution:
    
    def encode(self, strs: List[str]) -> str:
        holder = ""
        for i in strs:
            holder += i 
            holder += "!-@"
        return holder
    def decode(self, s: str) -> List[str]:
        temp = s.split("!-@")
        return temp[:-1]
