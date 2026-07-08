class Solution {
    public void duplicateZeros(int[] arr) {
        int[] ans= new int[arr.length];
        int k=0;
        for(int i=0;i<arr.length && k<arr.length;i++){
            if(arr[i]!=0){
                ans[k]=arr[i];
                k++;
            }
            else{
                ans[k]=arr[i];
                k++;
                if(k<arr.length){
                    ans[k]=arr[i];
                    k++;
                }
            }
        }
        for(int i=0;i<arr.length;i++){
            arr[i]=ans[i];
        }
    }
}