 import java.util.Scanner;

public class Handshakes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int totalHandshakes = (n * (n - 1)) / 2;
        System.out.println(totalHandshakes);
    }
}
