import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine().trim();
        String[] strArray = str.split(" ");
        if (str.isEmpty()) {
            System.out.println(strArray.length - 1);

        } else {
            System.out.println(strArray.length);
        }
    }
}