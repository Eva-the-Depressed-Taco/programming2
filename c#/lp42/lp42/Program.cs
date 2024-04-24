// See https://aka.ms/new-console-template for more information
Console.WriteLine("Enter Length!");
int length = int.Parse(Console.ReadLine());
Console.WriteLine("Enter width!");
int width = int.Parse(Console.ReadLine());
Console.WriteLine("Enter height!");
int height = int.Parse(Console.ReadLine());
Console.WriteLine("Enter weight!");
int weight = int.Parse(Console.ReadLine());

int volume = length * width * height;
if (weight > 27 && volume > 100000)
    Console.WriteLine("package is both to heavy and large");
else if (weight > 27)
    Console.WriteLine("package is to heavy");
else if (volume > 100_00)
    Console.WriteLine("package is to big");
else
    Console.WriteLine("package is ok..ig");

Console.ReadKey();