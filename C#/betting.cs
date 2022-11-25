using System;

public class Program 
    {
        public static void Main() 
            {
                float input = float.Parse(Console.ReadLine());
                float x1 = (input/100);
                float x2 = (1-x1);
                float y1 = (1/x1);
                float y2 = (1/x2);
                Console.WriteLine(string.Format("{0:00.##########}", y1));
                Console.WriteLine(string.Format("{0:00.##########}", y2));
            }
    }