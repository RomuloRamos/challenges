import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the plusMinus function below.
    static void plusMinus(int[] arr) {
        
        int iLength = arr.length;
        float fPositives = 0;
        float fNegatives = 0;
        float fZeros = 0;

        for(int iElements : arr)
        {
            if(iElements < 0 ) fNegatives++;
            else if(iElements == 0 ) fZeros++;
            else if(iElements > 0) fPositives++;
        }

        System.out.println(String.format("%.6f", (float)(fPositives/iLength)));
        System.out.println(String.format("%.6f", (float)(fNegatives/iLength)));
        System.out.println(String.format("%.6f", (float)(fZeros/iLength)));
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        plusMinus(arr);

        scanner.close();
    }
}
