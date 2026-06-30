class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs =  defaultdict(set)

        for i in range(0,9):
            for x in range (0,9):
                if(board[i][x] == "."):
                    continue
                
                if(board[i][x] in rows[i] 
                    or board[i][x] in cols[x] 
                    or board[i][x] in boxs[(i // 3,x // 3)]):
                    return False
                rows[i].add(board[i][x])
                cols[x].add(board[i][x])
                boxs[(i // 3,x // 3)].add(board[i][x])



        return True
