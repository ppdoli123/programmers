import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String number = sc.nextLine();
        String[] arr = number.split(" ");
        int max_num = 10;
        int min_num = 0;
        int min_count = 0;
        int max_count = 0;
        for (int i = 0; i < arr.length; i++) {
            if(Integer.parseInt(arr[i])<max_num){
                max_num = Integer.parseInt(arr[i]);
                min_count++;
            }
            if(Integer.parseInt(arr[i])>min_num){
                min_num = Integer.parseInt(arr[i]);
                max_count++;
            }
        }
        if(min_count == 8){
            System.out.println("descending");
    }
        else if(max_count == 8){
            System.out.println("ascending");
        }
        else{
            System.out.println("mixed");
        }
    }
}
