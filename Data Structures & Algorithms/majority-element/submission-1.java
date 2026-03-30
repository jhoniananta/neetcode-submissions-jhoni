class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num: nums){
            map.put(num, map.getOrDefault(num, 0)+1);
        }

        int max_val = 0;
        int max_freq = 0;

        for(Map.Entry<Integer, Integer> e: map.entrySet()){
            int key = e.getKey();
            int freq = e.getValue();
            if(freq > max_freq){
                max_freq = freq;
                max_val = key;
            }
        }
        return max_val;
    }
}