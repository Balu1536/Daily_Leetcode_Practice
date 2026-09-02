class Solution {
    public String shiftingLetters(String s, int[][] shifts) {

        int n = s.length();

        int[] diff = new int[n + 1];

        // Difference Array
        for (int[] shift : shifts) {

            int start = shift[0];
            int end = shift[1];
            int direction = shift[2];

            int value = (direction == 1) ? 1 : -1;

            diff[start] += value;
            diff[end + 1] -= value;
        }

        // Prefix Sum + build answer
        StringBuilder ans = new StringBuilder();

        int currentShift = 0;

        for (int i = 0; i < n; i++) {

            currentShift += diff[i];

            currentShift %= 26;

            if (currentShift < 0) {
                currentShift += 26;
            }

            char c = s.charAt(i);

            char newChar =
                (char) ('a' + (c - 'a' + currentShift) % 26);

            ans.append(newChar);
        }

        return ans.toString();
    }
}