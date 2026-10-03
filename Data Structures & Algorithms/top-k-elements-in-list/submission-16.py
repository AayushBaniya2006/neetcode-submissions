class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}

        for i in nums:
            temp[i] = temp.get(i, 0) + 1 

        buckets = [[] for i in range(len(nums))]
        
        for i in temp:
            buckets[temp.get(i)-1].append(i)
        ret = [0] * k 
        pos = 0
        for i in range(len(buckets)-1, -1, -1):
            for x in buckets[i]:
                print(pos)
                ret[pos] = x
                pos+=1 
                if pos>=k:
                    return ret
        print(ret)

         

           
                
        