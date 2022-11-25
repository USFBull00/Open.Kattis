using System;

public class Program 
    {
        public static void Main() 
            {
                int N = int.Parse(Console.ReadLine());
                int i = 1;
                while(i<=N)
                {
                    var input = Console.ReadLine();
                    string[] numbers = input.Split(" ");
                    int Number1 = int.Parse(numbers[0]);
                    int Number2 = int.Parse(numbers[1]);
                    int Number3 = int.Parse(numbers[2]);
                    int adv = (Number2-Number3);
                    if(Number1==adv)
                    {
                        Console.WriteLine("does not matter");
                    }
                    else if(Number1>adv)
                    {
                        Console.WriteLine("do not advertise");
                    }
                    else
                    {
                        Console.WriteLine("advertise");
                    }
                    i++;
                }
            }
    }