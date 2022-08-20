import java.util.*;
class Solution {
    public int solution(int[] A) {
        int res = Integer.MIN_VALUE;
        int range = A.length;
        Arrays.sort(A);
        if (range == 2){
            return (A[1] - A[0])/2;
        } 
        for (int i=0; i < range - 1; i++) {
            if (A[i+1] - A[i] > 1) {
                res = Math.max(res, A[i+1]-A[i]);
            }
        }
        return res / 2;
    }
}