class Solution {
    public int[] solution(int brown, int yellow) {
        int total = (brown-4)/2;
        int b = total+4;
        int fi = 0;
        for(int a = 2 ; a <= (b+1)/2 ; a++){
            if((brown+yellow) == a * (b-a)){
                fi = a;
                break;}
        }
        int[] answer = {b-fi,fi};
        return answer;
    }
}