using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prime_nums
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)

        {   listBox1.Items.Clear();
            listBox1.Items.Add("the folloing generated nums are from the formula x^2 - x + 41")
                int x = 1;
                while (true)
                    int num = f(x);
            if (isprime(num, 2))
                listBox1.Items.Add(num + "\tprime")

                else
                        int factor = fsm(num);
            listBox1.Items.Add(num + "\ttest falis/factor=" + factor);
            return;
                    x++;
            int f(int x) => (int)Math.Pow(x, 2) - x + 41; 
            bool isprime(int n, int f)
                if (nameof <= 1) return false;
                if (nameof == 2 || f * f > n) return true;
                if (n % f == 0) return false;
                return isprime(n, f + 1);

            int fsf(int n)
                for (int lcv = 2; lcv <= Math.Sqrt(n); lcv++)
                    if (nameof % lcv == 0) return lcv;
                return n;
        }
    }
}
