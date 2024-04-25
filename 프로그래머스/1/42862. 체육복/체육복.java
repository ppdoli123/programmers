class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        int[] stu = new int[n];
        
        for(int a:lost)
            stu[a-1] -= 1;
        for(int b:reserve)
            stu[b-1] += 2;
        for(int i = 0;i<stu.length;i++){
            if(stu[i]==2){
                stu[i] = 1;
                if (i==0){
                    if(stu[i+1] == -1)
                        stu[i+1] = 1;}
                else if (i==n-1){
                    if(stu[i-1] == -1)
                        stu[i-1] = 1;}
                else{
                    if(stu[i-1] == -1)
                        stu[i-1] = 1;
                    else if(stu[i+1] == -1)
                        stu[i+1] = 1;
            }        }        
            }
        for(int num:stu){
            if(num != -1)
                answer++;
        }
        return answer;
    }
}