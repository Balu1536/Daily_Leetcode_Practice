class Solution {
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] sameBranch=new int[nums.length];
        int id=0;
        sameBranch[0]=id;
        for(int i=1;i<nums.length;i++){
            if((nums[i]-nums[i-1])>maxDiff){
                id++;
            }
            sameBranch[i]=id;
        }

        boolean[] ans = new boolean[queries.length];
        for(int i=0;i<queries.length;i++){
            int u=queries[i][0],v=queries[i][1];
            ans[i]=(sameBranch[u]==sameBranch[v]);
        }
        return ans;
    }
}