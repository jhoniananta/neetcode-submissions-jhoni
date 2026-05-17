class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int res = 0;
        int temp = 0;
        for (int i : nums){
            if (i == 1){
                temp++;
            } else{
                temp = 0;
                res = Math.max(temp, res);
            }

            res = Math.max(temp, res);
        }
        return res;
    }
}   