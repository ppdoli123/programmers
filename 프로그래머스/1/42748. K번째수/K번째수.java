import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        List<Integer> li = new ArrayList<>();
        for(int i =0;i < commands.length ;i++){
            for(int start = commands[i][0]-1 ; start<commands[i][1];start++){
                li.add(array[start]);
            }
            Collections.sort(li);
            answer[i] = li.get(commands[i][2]-1);
            li.removeAll(li);
            }
        return answer;
    }
}