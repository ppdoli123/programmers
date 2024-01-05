class Solution {
    public int[] solution(String[] strlist) {
        int x = strlist.length;
        int[] answer = new int[x];
        int num = 0;
        for(String strlist1 : strlist){
            answer[num]=strlist1.length();
            num += 1;
        }
        return answer;
    }
}