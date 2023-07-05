class Solution {
    public int[] twoSum(int[] nums, int target) {
    	int[] result = null;
     	HashMap<Integer, Integer> numsMap = new HashMap<Integer, Integer>();
    	for (int i = 0; i < nums.length; i++) {
    		numsMap.put(nums[i], i);
    	}
    	

    	for (int i = 0; i < nums.length; i++) {
    		int contrast = target - nums[i];
    		if (numsMap.containsKey(contrast) && i != numsMap.get(contrast)) {
    			result = new int[]{i, numsMap.get(contrast)};
    		}
    	}
    	
    	return result;
    }
}