using System;

public class Program 
    {
        public static void Main() 
            {
                var input = Console.ReadLine();
                string[] numbers = input.Split(" ");
                int Number1 = int.Parse(numbers[0]);
                int Number2 = int.Parse(numbers[1]);
                if(Number1>Number2)
                {
                    Console.WriteLine("1");
                }
                else
                {
                    Console.WriteLine("0");
                }
            }
    }