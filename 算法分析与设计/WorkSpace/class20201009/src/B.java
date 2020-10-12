import java.util.Scanner;

public class B {
    public static void main(String[] args){
        //第一种方法
//        Scanner sc = new Scanner(System.in);
//        while(sc.hasNext()){
//            int num = sc.nextInt();
//            /*
//            * StringBuilder
//            * String
//            * StringBuffer
//            * */
//            StringBuilder sb = new StringBuilder();
//            boolean flag = false;
//            for (int i = 0; i < 32; i++) {
//                int bit = num<<i<0 ? 1:0;
//                if(bit==1){
//                    flag=true;
//                }
//                if(flag){
//                    sb.append(num<<i<0 ? 1:0);
//                }
//            }
//            if(!flag){
//                sb.append('0');
//            }
//            System.out.println(sb.toString());
//        }

        //方法2
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()){
            System.out.println(Integer.toBinaryString(sc.nextInt()));
        }
    }
}
