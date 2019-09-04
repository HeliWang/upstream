// Time Complexity O(Nlogn)
// https://leetcode.com/submissions/detail/171161324/
class Solution {
    public int shortestSubarray(int[] A, int K) {
        int ans = Integer.MAX_VALUE;
        TreeMap<Integer, Integer> map = new TreeMap<>();
        int sum = 0;
        map.put(0, -1);
        for (int i = 0; i < A.length; i++) {
            sum += A[i];
            Integer sub = map.floorKey(sum - K);
            while (sub != null) {
                ans = Math.min(ans, i - map.get(sub));
                map.remove(sub);
                sub = map.floorKey(sub);
            }
            map.put(sum, i);
        }

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }
}