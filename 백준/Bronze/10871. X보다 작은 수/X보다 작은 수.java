import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] inputI = sc.nextLine().split(" ");
        int numLength = Integer.parseInt(inputI[0]);
        int maxNum = Integer.parseInt(inputI[1]);
        int[] numArr = new int[numLength];
        String[] inputS = sc.nextLine().split(" ");
        for (int i = 0; i < inputS.length; i++) {
            if(maxNum > Integer.parseInt(inputS[i])){
                System.out.print(Integer.parseInt(inputS[i]));
                System.out.print(" ");
            };
            
        }
    }
}