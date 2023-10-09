impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {

        let mut ans:Vec<i32> = vec![1;nums.len()];
        let mut startProduct = 1;

        for (num, a) in nums.iter().zip(ans.iter_mut()) {
            *a *= startProduct;
            startProduct *= num;
        }
        
        startProduct = 1;
        for (num, a) in nums.iter().rev().zip(ans.iter_mut().rev()) {
            *a *= startProduct;
            startProduct *= num;
        }

        ans
    }
}