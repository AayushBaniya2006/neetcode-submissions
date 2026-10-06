class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initalColor = image[sr][sc]
        if color == initalColor:
            return image
        def dfs(sc, sr):
            r = len(image)
            c = len(image[0])
            if sc < 0 or sr < 0 or sr >= r or sc >= c or image[sr][sc] != initalColor:
                return 
            image[sr][sc] = color     
            dfs(sc-1,sr)
            dfs(sc,sr-1)
            dfs(sc+1,sr)
            dfs(sc,sr+1)
        dfs(sc,sr)
        return image