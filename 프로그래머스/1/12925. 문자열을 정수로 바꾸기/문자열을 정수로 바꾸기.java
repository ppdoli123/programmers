class Solution {
    public int solution(String s) {
        int answer = 0;
        for(int i =0; i<s.length() ; i++){
            char num = s.charAt(i);
            answer += num;
        }
        
        return Integer.valueOf(s);
    }
}