// See https://aka.ms/new-console-template for more information
Console.WriteLine("enter grade!");
double numgrade = double.Parse(Console.ReadLine());
char grade = ' ';
if (grade >= 90)
    grade = 'A';
else if (grade >= 80)
    grade = 'B';
else if (grade >= 80)
    grade = 'C';
else if (grade >= 70)
    grade = 'D';
else if (grade >= 60)
    grade = 'F';
Console.WriteLine(grade);

Console.ReadKey();


