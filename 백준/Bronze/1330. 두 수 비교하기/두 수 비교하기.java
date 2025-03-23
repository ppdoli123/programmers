import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String inputValues = bf.readLine();
        String[] str = inputValues.split(" ");
        if(Integer.parseInt(str[0]) > Integer.parseInt(str[1])){
            System.out.println('>');
        }
        else if (Integer.parseInt(str[0]) < Integer.parseInt(str[1])){
            System.out.println('<');
        }
        else{
            System.out.println("==");
        }}
    }
