import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
//        윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        if(num%4==0 && (num%100!=0 || num%400==0)){
            System.out.println(1);
        }
        else{
            System.out.println(0);
        }
    }

    }