class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        int result = 0;
        for(int i =0;i < words.length ;i++){
            int index = 0;
            if(i>0 && words[i-1].charAt(words[i-1].length()-1) != words[i].charAt(0)){
                result=i;
                i = words.length -1;
                break;
            }
            while(true){
                if(i!=index && words[i].equals(words[index])){
                    result = i;
                    i = words.length -1;
                    break;}
                if( index == i){
                    break;}
                index ++;
            }

            if(i == words.length-1)
                break;
        }
        if (result == 0){
            int[] a={0,0};
            return a;
        }
        answer[0] =(result%n)+1;
        answer[1] =(result/n)+1;

        return answer;
    }
}