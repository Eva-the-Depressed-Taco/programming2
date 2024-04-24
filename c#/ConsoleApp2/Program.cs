
Console.WriteLine("enter number of copies!");
int copies = int.Parse(Console.ReadLine());
double price = 0;
double cost = 0;
if (copies > 0 && copies <= 99) price = 0.30;
else if (copies > 99 && copies <= 499) price = 0.28;
else if (copies > 499 && copies <= 749) price = 0.27;
else if (copies > 749 && copies <= 1000) price = 0.26;
else if (copies > 1000) price = 0.25;
else Console.WriteLine("invald");
cost = price * copies;
Console.WriteLine("price per copy " +price);
Console.WriteLine("total cost " + cost);
Console.ReadKey();