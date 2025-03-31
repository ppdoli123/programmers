
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int index = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < index ; i++) {
            String[] s = sc.nextLine().split(" ");
            int a = Integer.parseInt(s[0]);
            int b = Integer.parseInt(s[1]);
            int c = Integer.parseInt(s[2]);
            int floor = c/a;
            int level = c%a;
            if(level == 0){
                level = a;
                floor -= 1;
            }
            System.out.println((level*100)+(floor+1));
        }
    }
}