import java.util.Scanner;

public class SimpleInterest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int P = scanner.nextInt();
        int T = scanner.nextInt();
        int R = scanner.nextInt();
        
        int simpleInterest = (P * T * R) / 100;
        
        System.out.println(simpleInterest);
    }
}
