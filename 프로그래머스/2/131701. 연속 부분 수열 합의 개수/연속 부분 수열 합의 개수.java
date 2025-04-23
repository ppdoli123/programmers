import java.util.*;
class Solution {
    public int solution(int[] elements) {
        int length_size = elements.length;
        int result = 0;
        int cnt = 0;
        Set<Integer> set_arr = new HashSet<>();
        while(cnt < length_size){
            result = 0;
            for(int i = 0 ; i < length_size ; i++){
                result += elements[(cnt+i) % length_size];
                set_arr.add(result);
                }
            
            cnt++;
        }
        // System.out.println(set_arr);
        return set_arr.size();
    }
    
}
//         int answer = 0;
//         int l =1 ;
//         // int[] arr = new int[10000];
//         int a =0;
//         while(l < elements.length){
//             for(int idx = 0; idx < elements.length; idx ++ ){
//                 for(int t = idx ; t <= idx + l ; t ++){
//                     if(t >= elements.length){
//                         t = t %(elements.length-1);
//                     }
//                     answer += elements[t];
//                     System.out.println(answer);
//                 // arr[a] = answer ;
//                 a ++;

//                     }
//             }
//            l ++;}
        
//         return answer;
//     }
