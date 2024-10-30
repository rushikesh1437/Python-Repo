 import java.util.Scanner;

public class PolygonDiagonals {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int diagonals = (N * (N - 3)) / 2;
        System.out.println(diagonals);
    }
}
