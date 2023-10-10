class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def is_valid_sequence(sequence):
            # Filter out the empty cells '.'
            nums = [num for num in sequence if num != '.']
            return len(nums) == len(set(nums))

        # Check each row
        for row in board:
            if not is_valid_sequence(row):
                return False

        # Check each column
        for col in range(9):
            if not is_valid_sequence([board[row][col] for row in range(9)]):
                return False

        # Check each 3x3 box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not is_valid_sequence(box):
                    return False

        return True


        
        

        