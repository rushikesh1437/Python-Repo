 import java.util.Scanner;

public class MeetingSubscription {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int X = scanner.nextInt();
        
        if (X > 40) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
