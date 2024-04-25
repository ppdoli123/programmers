class Solution {
    public String solution(String s) {
        String answer = "";
        
        System.out.println(s.length());
        if(s.length()%2==0){
            answer += s.charAt(s.length()/2-1);
            answer += s.charAt(s.length()/2);}
        else
            answer += s.charAt((int) s.length()/2);
        return answer;
    }
}