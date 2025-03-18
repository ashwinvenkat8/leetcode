class Solution {
    public int sum(int startIndex, int endIndex, int[] nums) {
        int result = 0;
        
        for (int i = startIndex; i <= endIndex; ++i) {
            result += nums[i];
        }
        
        return result;
    }
    
    public int pivotIndex(int[] nums) {
        int pivotIndex = -1;
        
        for (int i = 0; i < nums.length; ++i) {
            int leftSum = 0, rightSum = 0;
            
            if(i == 0) {
                leftSum = 0;
                rightSum = sum(i+1, nums.length-1, nums);
            }
            else if (i <= nums.length-2) {
                leftSum = sum(0, i-1, nums);
                rightSum = sum(i+1, nums.length-1, nums);
            }
            else {
                rightSum = 0;
                leftSum = sum(0, nums.length-2, nums);
            }
            
            if (leftSum == rightSum) {
                pivotIndex = i;
                break;
            }
        }
        
        return pivotIndex;
    }
}