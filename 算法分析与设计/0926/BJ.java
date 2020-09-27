import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        String string = cin.next();
        StringBuffer tring = new StringBuffer(string);
        tring.reverse();//利用Java的重置函数功能
        System.out.println(string + tring.toString());
        cin.close();
    }
}