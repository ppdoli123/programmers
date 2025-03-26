import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            String[] num = sc.nextLine().split(" ");
            System.out.println(Integer.parseInt(num[0]) + Integer.parseInt(num[1]));
        }

        }
    }
