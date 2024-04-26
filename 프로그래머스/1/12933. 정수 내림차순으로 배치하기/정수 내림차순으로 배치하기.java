import java.util.*;
class Solution {
    public long solution(long n) {
        long answer = 0;
        String b= String.valueOf(n);
        String[] ab = b.split("");
        List<Integer> in = new ArrayList<>();
        for(int i=0;i<ab.length;i++){
            in.add(Integer.parseInt(ab[i]));
        }
        Collections.sort(in);
        String a ="";
        for(int q = in.size()-1 ; q>=0;q--){
            a += String.valueOf(in.get(q));
        }
        answer = Long.parseLong(a);
        return answer;
    }
}