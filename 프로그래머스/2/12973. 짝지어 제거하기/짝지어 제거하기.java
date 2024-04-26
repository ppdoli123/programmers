import java.util.*;
class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        Stack<Character> st = new Stack<>();
        st.push(s.charAt(0));
        for(int i=1;i<s.length();i++){
            if(!st.empty()){
                if(st.peek() == s.charAt(i)){
                    st.pop();
                }
                else
                    st.push(s.charAt(i));
            }
            else
                st.push(s.charAt(i));
            
        }
        if(st.empty()){
            answer = 1;
        }
        else{
            answer = 0;
        }

        return answer;
    }
}