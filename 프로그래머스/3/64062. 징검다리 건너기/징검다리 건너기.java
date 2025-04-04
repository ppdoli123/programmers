import java.lang.*;
class Solution {
    public int solution(int[] stones, int k) {
        int right = Integer.MAX_VALUE;
        int left = 0;
        int max = 0;
        while(left <= right){
            int mid = (right+left) / 2;
            int count = 0;
            int i = 0;
            for(i = 0 ; i < stones.length; i++) {
                if(stones[i] - mid < 0){
                    count ++; 
                    if(count == k){
                        right = mid-1;
                        break;
                    }
                }
                else{
                    count = 0;
                }
            }
            if(count < k){
                left = mid + 1;
            }
        }
        return Math.min(left,right);
    }
}
