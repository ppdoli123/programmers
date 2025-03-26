import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String num1 = sc.nextLine();
        String num2 = sc.nextLine();
        String num3 = sc.nextLine();

        System.out.println(Integer.parseInt(num1)+Integer.parseInt(num2)-Integer.parseInt(num3));
        String numPlus = num1+num2;
        System.out.println(Integer.parseInt(numPlus)-Integer.parseInt(num3));
    }

    }