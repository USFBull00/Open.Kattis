using System;

public class Program 
    {
        public static void Main() 
            {
                var input = Console.ReadLine();
                string[] numbers = input.Split(" ");
                int Number1 = int.Parse(numbers[0]);
                int Number2 = int.Parse(numbers[1]);
                int Number3 = int.Parse(numbers[2]);
                int combinations = (Number1*Number2*Number3);
                Console.WriteLine(combinations);
            }
    }