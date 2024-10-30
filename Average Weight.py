 import java.util.Scanner;

public class ThirdBoyWeight {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int average = scanner.nextInt();
        int W1 = scanner.nextInt();
        int W2 = scanner.nextInt();
        int W3 = (3 * average) - (W1 + W2);
        System.out.println(W3);
    }
}
