
import java.util.Scanner;

public class Monopoly {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int R1 = scanner.nextInt();
            int R2 = scanner.nextInt();
            int R3 = scanner.nextInt();

            if (R1 > R2 + R3 || R2 > R1 + R3 || R3 > R1 + R2) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
