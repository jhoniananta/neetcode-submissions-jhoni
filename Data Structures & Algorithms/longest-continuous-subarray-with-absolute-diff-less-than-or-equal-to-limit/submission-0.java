class Solution {
    public int longestSubarray(int[] nums, int limit) {
        int res = 1;
        for (int i = 0; i < nums.length; i++){
            int mini = nums[i], maxi = nums[i];
            for (int j = i + 1; j < nums.length; j++) {
                mini = Math.min(mini, nums[j]);
                maxi = Math.max(maxi, nums[j]);

                if ((maxi - mini) > limit){
                    break;
                }
                res = Math.max(res, j - i + 1);
            }
        }

        return res;
    }
}