import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String[] s = sc.nextLine().split(" ");
        int[] i = new int[2];
        i[0] = Integer.parseInt(s[0]);
        i[1] = Integer.parseInt(s[1]);
        if(i[1]-45<0){
            i[1] += 15;
            i[0] -= 1;
        }
        else{
            i[1] -= 45;
        }
        if(i[0]<0){
            i[0] = 23;
        }
        System.out.println(i[0]+" "+i[1]);

    }
}