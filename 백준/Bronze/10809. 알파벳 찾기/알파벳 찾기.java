
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] alphabat = new int[26];
        for (int i = 0; i < alphabat.length; i++) {
            alphabat[i] = -1;
        }
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        for(int i=0;i<str.length(); i++) {
            if (alphabat[str.charAt(i) - 'a'] == -1) {
                alphabat[str.charAt(i) - 'a'] = i;
            }
        }
        for (int j = 0; j < 26; j++) {
            System.out.print(alphabat[j] + " ");
        }
    }
}
