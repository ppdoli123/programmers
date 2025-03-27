import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < num; i++) {
            int result = 0;
            String[] strArr = sc.nextLine().split("");
            int count = 0;
            for(String str : strArr){
                if(str.equals("O")){
                    count ++;
                    result += count;
                }
                else count=0;
            }
            System.out.println(result);
        }
    }

    }