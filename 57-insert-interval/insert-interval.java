class Solution {

    public int[][] insert(int[][] intervals, int[] newInterval) {

        int n = intervals.length;

        // Maximum possible intervals = n + 1
        int[][] ans = new int[n + 1][2];

        int i = 0;
        int k = 0;

        // Step 1: Copy all intervals before newInterval
        while (i < n && intervals[i][1] < newInterval[0]) {

            ans[k][0] = intervals[i][0];
            ans[k][1] = intervals[i][1];

            k++;
            i++;
        }

        // Step 2: Merge overlapping intervals
        while (i < n && intervals[i][0] <= newInterval[1]) {

            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);

            i++;
        }

        // Store merged interval
        ans[k][0] = newInterval[0];
        ans[k][1] = newInterval[1];

        k++;

        // Step 3: Copy remaining intervals
        while (i < n) {

            ans[k][0] = intervals[i][0];
            ans[k][1] = intervals[i][1];

            k++;
            i++;
        }

        // Create exact size result
        int[][] result = new int[k][2];

        for (int j = 0; j < k; j++) {
            result[j][0] = ans[j][0];
            result[j][1] = ans[j][1];
        }

        return result;
    }
}