class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        int[] ans=new int[nums.length];
        int size=0;
        for(int i=0;i<index.length;i++){
            for(int j=size;j>index[i];j--){
                ans[j]=ans[j-1];
            }
            ans[index[i]]=nums[i];
            size++;
        }
        return ans;
    }
}