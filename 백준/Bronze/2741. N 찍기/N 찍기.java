import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        // Scanner sc = new Scanner(System.in);
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String inputValues = bf.readLine();
        for(int i=1;i <= Integer.parseInt(inputValues); i++){
            System.out.println(i);
        }
    }
}
