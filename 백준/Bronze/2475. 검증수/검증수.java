import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] nums = sc.nextLine().split(" ");
        int sum = 0;
        for(String num:nums){
            int number = Integer.parseInt(num);
            sum += (number)*(number);
        }
        System.out.println(sum%10);
    }

    }