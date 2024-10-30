import java.util.Scanner;

public class PowerMod {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int m = scanner.nextInt();
        long result = 1;
        for (int i = 0; i < y; i++) {
            result = (result * x) % m;
        }
        System.out.println(result);
    }
}
