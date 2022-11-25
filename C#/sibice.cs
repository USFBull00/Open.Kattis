using System;

namespace Kattis
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine();
            string[] numbers = input.Split(' ');
            var N = int.Parse(numbers[0]);
            var Width = int.Parse(numbers[1]);
            var Height = int.Parse(numbers[2]);
            var Max = Math.Sqrt(Math.Pow(Width, 2) + Math.Pow(Height, 2));

            for(int i =1; i<=N; i++)
            {
                var value = int.Parse(Console.ReadLine());
                if (value <= Max)
                    Console.WriteLine("DA");
                else
                    Console.WriteLine("NE");
            }
        }
    }
}