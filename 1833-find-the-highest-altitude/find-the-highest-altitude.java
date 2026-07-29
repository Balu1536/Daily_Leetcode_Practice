class Solution {
    public int largestAltitude(int[] gain) {
        int present=0, altitude=0;
        for(int i=0;i<gain.length;i++){
            present+=gain[i];
            altitude=Math.max(altitude,present);
            
        }
        return altitude;
    }
}