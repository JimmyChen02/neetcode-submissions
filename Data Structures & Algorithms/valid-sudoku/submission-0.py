class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        #check cols
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
        #check each 3x3 box
        for i in range(0,8,3):
            for j in range(0, 8,3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        if board[i+r][j+c] != '.':
                            if board[i+r][j+c] in seen:
                                return False
                            seen.add(board[i+r][j+c])
        return True
