import java.util.Arrays;
import java.util.Scanner;

public class D {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int T,N;
        T=sc.nextInt();
        while(T> 0){
            N = sc.nextInt();
            int[] arr = new int[2*N];
            for (int i = 0; i < 2*N; i++) {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);

            boolean[] flags = new boolean[200];
            // 布尔类型的初始值为 false
            for (int j = 0; j < 2*N; j++) {
                if(flags[arr[j]]==false){
                    System.out.printf("%d ",arr[j]);
                    flags[arr[j]]=true;
                }
            }
            System.out.println();
            T--;
        }
    }

}

