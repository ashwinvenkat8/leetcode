class Solution {
    public int dominantIndex(int[] nums) {
        if(nums.length == 1)
            return 0;

        int largeNumIndex = 0;
        int largeNum = nums[largeNumIndex];
        boolean domIndex = true;

        for(int i = 1; i < nums.length; ++i) {
            if (nums[i] > largeNum) {
                largeNum = nums[i];
                largeNumIndex = i;
            }
        }

        for(int i = 0; i < nums.length; ++i)
            if ((i != largeNumIndex) && (largeNum < 2*nums[i]))
                domIndex = false;

        if(domIndex)
            return largeNumIndex;

        return -1;
    }
}