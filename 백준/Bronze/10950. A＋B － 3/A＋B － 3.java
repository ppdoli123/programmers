import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < n; i++) {
            String[] num = sc.nextLine().split(" ");
            System.out.println(Integer.parseInt(num[0]) + Integer.parseInt(num[1]));
        }

        }
    }
