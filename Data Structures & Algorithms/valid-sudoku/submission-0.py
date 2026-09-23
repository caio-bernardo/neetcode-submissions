class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each row must contain a single digit
        for row in board:
            seen = [False] * 10
            for cell in row:
                if cell.isdigit():
                    num = int(cell)
                    if seen[num]:
                        return False
                    else:
                        seen[num] = True
        # each column must contain a single digit
        for col in zip(*board):
            seen = [False] * 10
            for cell in col:
                if cell.isdigit():
                    num = int(cell)
                    if seen[num]:
                        return False
                    else:
                        seen[num] = True
        
        # each grid is valid
        n = len(board)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                seen = [False] * 10
                for offset_i in range(0, 3):
                    for offset_j in range(0, 3):
                        cell = board[i + offset_i][j + offset_j]
                        if cell.isdigit():
                            num = int(cell)
                            if seen[num]:
                                return False
                            else:
                                seen[num] = True

        return True