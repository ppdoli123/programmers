import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int num1 = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < num1; i++) {
            System.out.println(num1-i);
        }
    }
}
