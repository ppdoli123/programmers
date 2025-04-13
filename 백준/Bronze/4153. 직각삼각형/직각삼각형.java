import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            String[] arr = sc.nextLine().split(" ");
            int[] intarr = {Integer.parseInt(arr[0]),Integer.parseInt(arr[1]),Integer.parseInt(arr[2])};
            if(intarr[0] == 0 || intarr[1] == 0 || intarr[2] == 0){
                break;
            }
            else{
                if(Math.pow(intarr[0],2)+Math.pow(intarr[1],2) == Math.pow(intarr[2],2)){
                    System.out.println("right");
                }
                else if(Math.pow(intarr[0],2)+Math.pow(intarr[2],2) == Math.pow(intarr[1],2)){
                    System.out.println("right");
                }
                else if(Math.pow(intarr[2],2)+Math.pow(intarr[1],2) == Math.pow(intarr[0],2)){
                    System.out.println("right");
                }
                else{
                    System.out.println("wrong");
                }
            }
        }
    }
}
