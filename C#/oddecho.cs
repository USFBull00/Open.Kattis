using System;

public class Program 
    {
        public static void Main() 
            {
               int N = int.Parse(Console.ReadLine());
               for(int i=1; i<=N; i++)
               {
                   var line = Console.ReadLine();
                   if(i%2 == 1)
                   {
                       Console.WriteLine(line);
                   }
               }
            }
    }