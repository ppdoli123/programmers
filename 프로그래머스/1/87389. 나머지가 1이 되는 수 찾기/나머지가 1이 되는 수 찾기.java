class Solution {
    public int solution(int n) {
        int answer = 0;
        int i = 2;
        while(i<n){
            if(n%i == 1){
                answer=i;
                break;
            }
            i++;
        }
        return answer;
    }
}