import java.util.Arrays;
import java.util.Scanner;

public class A {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[6];
        for (int i = 0; i < 6; i++) {
            arr[i]=sc.nextInt();
        }
        Arrays.sort(arr);
        for (int i = 5; i >= 0; i--) {
            System.out.print(arr[i]);
        }
    }
}
