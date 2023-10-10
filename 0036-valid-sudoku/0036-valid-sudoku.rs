use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut sets: Vec<HashSet<char>> = vec![HashSet::new(); 27];

        for row in 0..9 {
            for col in 0..9 {
                let num = board[row][col];
                    if num != '.' {
                        let row_idx = row;
                        let col_idx = col + 9;
                        let box_idx = 18 + (row / 3) * 3 + (col / 3);

                        if sets[row_idx].contains(&num) || sets[col_idx].contains(&num) || sets[box_idx].contains(&num){
                            return false
                        }

                        sets[row_idx].insert(num);
                        sets[col_idx].insert(num);
                        sets[box_idx].insert(num);
                    }
            }
        }
        true

        
    }
}