class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        temp = {}

        for i in nums:
            if i not in temp: 
                temp[i] = 0
            temp[i] = temp[i] + 1

        print(temp)
        holder = [[] for i in range(len(nums) + 1)]
        for n, c in temp.items():
            holder[c].append(n)

        pos = 0
        ret = [0] * k
        for i in range(len(nums), 0, -1):
            for x in holder[i]:
                ret[pos] = x
                pos += 1
                if(pos == k):
                    return ret
        return []