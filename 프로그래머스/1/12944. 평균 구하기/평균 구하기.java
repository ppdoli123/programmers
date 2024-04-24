class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int count = 0;
        for(int i : arr){
            answer+= i;
            count ++;
        }
        return answer/count;
    }
}