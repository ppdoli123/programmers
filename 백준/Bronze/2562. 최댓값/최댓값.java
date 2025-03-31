
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int MAX_VALUE = 0;
        int MAX_INDEX = 0;
        for (int i = 0; i < 9; i++) {
            int num = sc.nextInt();
            if (MAX_VALUE < num) {
                MAX_VALUE = num;
                MAX_INDEX = i+1;
            }
        }
        System.out.println(MAX_VALUE);
        System.out.println(MAX_INDEX);
    }
}