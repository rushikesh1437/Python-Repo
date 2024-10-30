 import java.util.Scanner;

public class StairClimber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        
        for (int i = 0; i < T; i++) {
            int X = scanner.nextInt();
            int Y = scanner.nextInt();

            int moves = X / Y; 
            int remainingSteps = X % Y; 
            if (remainingSteps > 0) {
                moves += remainingSteps; 
            }

            System.out.println(moves);
        }
    }
}
