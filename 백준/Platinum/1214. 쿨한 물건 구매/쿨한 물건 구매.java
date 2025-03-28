
import java.util.*;
import java.io.*;
//큰놈으로 최대값 넣고 하나씩 빼가면서 감소 if 증가하면 답
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");

        int num = Integer.parseInt(str[0]);
        int big_num = Integer.parseInt(str[1]) > Integer.parseInt(str[2]) ? Integer.parseInt(str[1]) : Integer.parseInt(str[2]);
        int small_num = Integer.parseInt(str[1]) < Integer.parseInt(str[2]) ? Integer.parseInt(str[1]) : Integer.parseInt(str[2]);

        int minResult = Integer.MAX_VALUE;

        for (int i = 0; i <= big_num; i++) {
            if (small_num * i > num) {
                minResult = Math.min(minResult, small_num * i);
                break;
            } else {
                int q = (num - small_num * i) / big_num;
                if (big_num * q + small_num * i == num) {
                    System.out.println(big_num * q + small_num * i);
                    return;
                } else {
                    minResult = Math.min(minResult, big_num * (q + 1) + small_num * i);
                }
            }
        }

        System.out.println(minResult);
    }
}
//        }
//        while(big_num*indexT<=num){
//            int tmp = num-big_num*indexT;
//            int div = tmp / small_num;
//            if((div*small_num)!=tmp){
//                div++;
//            }
//
//            int answer = big_num*indexT+small_num*div;
//
//            if(list.get(0) > answer){
//                list.remove(0);
//                list.add(answer);
//            }
//            indexT++;
//        }
//