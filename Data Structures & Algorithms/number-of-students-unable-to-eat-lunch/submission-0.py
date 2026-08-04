class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        temp = deque()
        notAte = 0
        sandPos = 0
        for i in students:
            temp.append(i)

        while notAte < len(temp):
            if(temp[0] == sandwiches[sandPos]):
                temp.popleft()
                sandPos += 1
                notAte = 0
            else: 
                notAte += 1
                temp.append(temp.popleft())
        return len(temp)