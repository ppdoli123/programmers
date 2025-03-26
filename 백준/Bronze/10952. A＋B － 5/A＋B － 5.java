import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true) {
            String[] num = sc.nextLine().split(" ");
            if (num[0].equals("0") && num[1].equals("0")) {
                break;
            } else {
                System.out.println(Integer.parseInt(num[0]) + Integer.parseInt(num[1]));
            }
        }

    }
}
