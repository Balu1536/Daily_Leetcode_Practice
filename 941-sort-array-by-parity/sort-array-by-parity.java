class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int f=0,l=nums.length-1;
        while(f<l){
            if(nums[f]%2!=0 && nums[l]%2==0){
                int temp=nums[f];
                nums[f]=nums[l];
                nums[l]=temp;
            }
            if(nums[f]%2==0)f++;
            if(nums[l]%2!=0)l--;
        }
        return nums;
    }
}