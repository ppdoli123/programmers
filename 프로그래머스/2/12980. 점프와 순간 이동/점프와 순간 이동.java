import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;
        int count = 0;
        if (n%2==1){
            n-=1;
            count+=1;
        }
        if(n==1){
            return 1;
        }
        while(n>1){
            n=n/2;

            if (n%2==1){
                n-=1;
                count+=1;
            }           
            
        }
        return count;
    }
}