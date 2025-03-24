import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int num1 = Integer.parseInt(sc.nextLine());
        int num2 = Integer.parseInt(sc.nextLine());

        if(num1 > num2){
            System.out.println("flight");
        }
        else{
            System.out.println("high speed rail");
        }
    }
}
