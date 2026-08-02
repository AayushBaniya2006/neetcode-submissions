class Solution:
    def calPoints(self, operations: List[str]) -> int:
        holder = []
        temp = 0
        temp2 = 0
        for x in operations:
            if x == '+':
                temp = holder.pop()
                temp2 = holder[-1]
                holder.append(temp)
                holder.append(temp + temp2)
            elif x == 'C':
                holder.pop()
            elif x == 'D':
                holder.append(int(holder[-1] * 2))
            else: 
                holder.append(int(x))
        print(holder)

        temp = 0
        for i in holder:
            temp += i 

        return temp



