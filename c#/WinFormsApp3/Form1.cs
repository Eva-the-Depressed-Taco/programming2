namespace WinFormsApp3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int rad = int.Parse(textBox1.Text);
                double area = rad * 3.14;
                label1.Text = area.ToString();




        }
    }
}