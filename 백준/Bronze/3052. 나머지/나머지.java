
import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> numList = new HashSet<>();
        while(sc.hasNext()){
            int num = Integer.parseInt(sc.nextLine());
            numList.add(num%42);
        }
        System.out.println(numList.size());
    }
    }