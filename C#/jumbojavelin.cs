using System;

public class Program 
    {
        public static void Main() 
            {
                int N = int.Parse(Console.ReadLine());
                int i = 1;
                int sum = 0;
                while(i<=N)
                {
                    int input = int.Parse(Console.ReadLine());
                    sum += input;
                    i++;
                }
                int loss = (N-1);
                int total = (sum-loss);
                Console.WriteLine(total);
            }
    }