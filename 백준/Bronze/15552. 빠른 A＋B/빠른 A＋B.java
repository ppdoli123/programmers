import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        // Scanner sc = new Scanner(System.in);
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String inputValues = bf.readLine();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i=0;i < Integer.parseInt(inputValues) ; i++){
            String[] values = bf.readLine().split(" ");
            bw.write(Integer.toString(Integer.parseInt(values[0]) + Integer.parseInt(values[1]))+"\n");

        }
        bw.flush();
        bw.close();
    }
}
