class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();

        Arrays.sort(nums);

        for (int i=0; i<nums.length-2; i++){
            if(i > 0 && nums[i] == nums[i-1]) continue; // skip juga duplikat
            int left = i+1, right = nums.length-1;

            while (left<right){
                int sum = nums[left] + nums[right] + nums[i];

                if(sum == 0){
                    answer.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    //skip duplikat
                    while(left < right && nums[left] == nums[left+1]) left++;
                    while(left < right && nums[right] == nums[right-1]) right--;

                    left++;
                    right--;
                } else if (sum<0){
                    left++;
                } else {
                    right--;
                }
            }
        }

        return answer;
    }
}
