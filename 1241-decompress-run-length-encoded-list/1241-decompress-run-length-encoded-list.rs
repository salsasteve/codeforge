impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {

        let mut ans:Vec<i32> = Vec::new();

        for pair in nums.chunks(2) {
            let freq = pair[0];
            let val  = pair[1];
            for _ in 0..freq {
                ans.push(val);
            }
        }
        
        ans
    }
}