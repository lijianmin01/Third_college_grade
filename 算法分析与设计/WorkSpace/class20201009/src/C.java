import java.util.Scanner;

public class C {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N,K;
        N=sc.nextInt();
        K=sc.nextInt();
        boolean[] arr=new boolean[N+1];

        for (int i = 1; i <=K ; i++) {
            for (int j = i; j <=N; j+=i) {
                arr[j]=!arr[j];
            }
        }

        for (int i = 0; i <= N; i++) {
            if(arr[i]){
                System.out.print(i+" ");
            }
        }
        System.out.println();
    }
}
