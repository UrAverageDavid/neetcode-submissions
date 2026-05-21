class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # the most obvious thing to do would be to do 2 n^2 sweeps for the large & small board,
        # but that is hella inefficient
        # alternate solution:
        # keep row, column, and grid sets in individual bits
        # nested for loop, scan each element and add the frequency into saved data, reset if we move on
        # technically O(n), since we only traverse each cell once
        # we trade memory for time efficiency
        horizontal = [0] * 9
        vertical = [0] * 9
        box = [0] * 9
        # box index: 0/3/6
        for i in range(len(board)):
            for j in range(len(board[0])):
                item = board[i][j]
                if item == ".": continue
                else:
                    digit = 1 << (int(item) - 1)
                    r, c, b = i, j, (i // 3) * 3 + j // 3 
                    if horizontal[r] & digit or vertical[c] & digit or box[b] & digit:
                        return False
                    else:
                        horizontal[r] |= digit
                        vertical[c] |= digit
                        box[b] |= digit
        return True             

        