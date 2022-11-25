using System;

public class Program 
    {
        public static void Main() 
            {
                var input = Console.ReadLine();
                string[] numbers = input.Split(" ");
                int Number1 = int.Parse(numbers[0]);
                int Number2 = int.Parse(numbers[1]);
                float square = (Number1*Number2);
                float triangle = (square/2);
                Console.WriteLine(triangle);
            }
    }