import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String inputValues = bf.readLine();
        String[] str = inputValues.split(" ");
        System.out.println(Integer.parseInt(str[0])*Integer.parseInt(str[1]));
        }
    }
