class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxV = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > maxV:
                temp = arr[i]
                arr[i] = maxV
                maxV = temp
            else: 
                arr[i] = maxV
        return arr