class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return 0;

        int m = matrix.length;
        int n = matrix[0].length;

        int res = 0;

        for (int i=0; i<m ;i++) {
            int[] row_sum = new int[n];
            for (int k=i; k<m; k++) {
                for (int j=0; j<n; j++) {
                    row_sum[j] += matrix[k][j];
                }
                res += find_target_in_array(row_sum, target);
            }
        }
        return res;
    }

    private int find_target_in_array(int[] arr, int target) {
        Map<Integer, Integer> hm = new HashMap<>();
        int res = 0;
        int sum = 0;
        hm.put(0, 1);
        for (int i=0; i<arr.length; i++) {
            sum += arr[i];

            if (hm.containsKey(sum-target)) {
                res += hm.get(sum-target);
            }
            int prev_v = hm.getOrDefault(sum, 0);
            hm.put(sum, prev_v+1);
        }

        return res;
    }
}