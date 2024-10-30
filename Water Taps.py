import java.util.Scanner;

public class TankFilling {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        
        double rateA = 1.0 / A; 
        double rateB = 1.0 / B; 
        
        double combinedRate = rateA + rateB; 
        double timeToFill = 1.0 / combinedRate; 
        
        System.out.println((int)Math.ceil(timeToFill)); 
    }
}
