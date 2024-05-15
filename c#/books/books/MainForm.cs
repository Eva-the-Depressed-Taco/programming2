/*
 * Created by SharpDevelop.
 * User: white.e
 * Date: 5/15/2024
 * Time: 2:33 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace books
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		
		void Button1Click(object sender, EventArgs e)
		{
			int b = int.Parse(textBox1.Text);
            int points = 0;
            
            if (b == 0)
                points = 0;
            if (b == 1)
                points = 5;
            if (b == 2)
                points = 15;
            if (b == 3)
                points = 30;
            if (b > 3)
                points = 60;
            label1.Text = points.ToString();
           
		}
	}
}
