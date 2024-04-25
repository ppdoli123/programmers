class Solution {
    public String solution(String s) {
        String[] i = s.split(" ");
        int n =0;
        int[] num = new int[i.length];
        int a=0;
        for(String e : i){
            num[a] = Integer.valueOf(e);
            System.out.println(num[a]);
            a++;
        }
        int max = -1000000;
        int min = 10000000;
        for(int aa : num){
            if(aa > max)
                max = aa;
            if(aa < min)
                min = aa;
        }
//         for(int a=0;a<s.length();a+=2){
//             i[n] = s.charAt(a)-48;
            
//             System.out.println(i[n]);
//             n += 1;
//         }
        String answer = "";
        return min+" "+max;
    }
}