class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left=0, right=numbers.length-1;
        int[] output = new int[2];

        while(left<right){
            int sum=numbers[left]+numbers[right];

            if(sum==target){
                output[0] = left+1;
                output[1] = right+1;
                break;
            }
            else if(sum<target){
                left++;
                continue;
            }
            else if(sum>target){
                right--;
                continue;
            }
        }

        return output;
    }
}
