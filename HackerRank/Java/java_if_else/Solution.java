package Java.java_if_else;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        if (n % 2 == 1)
            System.out.println("Weird");
        else {
            if (n >= 2 && n <= 5)
                System.out.println("Not Weird");
            else if (n <= 20)
                System.out.println("Weird");
            else
                System.out.println("Not Weird");
        }
        bufferedReader.close();
    }
}

