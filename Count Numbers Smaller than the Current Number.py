 import java.util.Scanner;

public class SmallerNumbersCount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && nums[j] < nums[i]) {
                    result[i]++;
                }
            }
        }
        
        for (int count : result) {
            System.out.print(count + " ");
        }
    }
}
