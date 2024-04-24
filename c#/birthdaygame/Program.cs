// See https://aka.ms/new-console-template for more information
Console.WriteLine("Enter birth month num, eg jan = 1, etc");
int month = int.Parse(Console.ReadLine());
Console.WriteLine("Enter birth day num, eg 10th = 10, etc");
int day = int.Parse(Console.ReadLine());
double n1 = (month * 5);
double n2 = (n1 + 6);
double n3 = (n2 * 4);
double n4 = n3 + 9;
double n5 = n4 * 5;
double n6 = n5 + day;
Console.WriteLine("your birthday is " + month + "/" + day);
Console.WriteLine("your number is " + n6);
Console.ReadKey();
