class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # One list to hold all the sets. Each set ensures no repetition.
        # 0-8: rows, 9-17: columns, 18-26: boxes
        sets = [set() for _ in range(27)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                # Indexes for the row, column, and box sets
                row_idx, col_idx, box_idx = i, 9 + j, 18 + (i // 3) * 3 + j // 3
                
                if num in sets[row_idx] or num in sets[col_idx] or num in sets[box_idx]:
                    return False
                
                sets[row_idx].add(num)
                sets[col_idx].add(num)
                sets[box_idx].add(num)
                
        return True
                        


        
        

        