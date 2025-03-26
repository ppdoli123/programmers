import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String numN = sc.nextLine();
        int sum = 0;
        String[] num = sc.nextLine().split("");
        for(int i=0;i < num.length ; i++){
            sum += Integer.parseInt(num[i]);
        }
        System.out.println(sum);
    }

    }