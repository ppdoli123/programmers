class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        int[] num = {};
        int result = 0;
        for(int num1 = 0; num1 < n ; num1++){
            result = arr1[num1]|arr2[num1];
            int compare = 0;
            int i=n-1;
            answer[num1] = "";
            String s ="";
            while(true){
                compare += Math.pow(2,i);
                if(compare > result){
                    compare -= Math.pow(2,i);
                    s += " ";
                }
                else
                    s += "#";
                if(compare == result){
                    while(true){
                        if(s.length() == n)
                            break;
                        s += " ";
                    }
                    answer[num1] += s;
                    break;}
                i--;
            }
        }
        return answer;
    }
}