 
 import java.util.Scanner;

public class FeverCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        
        if (X > 98) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
