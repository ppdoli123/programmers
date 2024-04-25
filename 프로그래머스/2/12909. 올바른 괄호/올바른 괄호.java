class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int first = 0;
        int last = 0;
        for(int i =0;i<s.length();i++){
            if(s.charAt(i) == '(')
                first ++;
            else
                first --;
            if(first <0)
                return false;
        }
        if (first == 0)
            return true;
        else
            return false;
//                 int index=i;
//                 while(true){
//                     if(s.charAt(index) == ')')
//                         break;
                    
//                     if(s.length()-1 == index){
//                         answer= false;
//                         break;
//                     }

//                     index++;
//                 }
//                 System.out.println();
//             }

    }
}