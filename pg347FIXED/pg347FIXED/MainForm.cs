/*
 * Created by SharpDevelop.
 * User: white.e
 * Date: 5/3/2024
 * Time: 2:33 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace pg347FIXED
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
			int n = int.Parse(textBox1.Text);
			int n2 = int.Parse(textBox2.Text);
			int A = n + n2;
			label1.Text = A.ToString();sz}
	}
}
	

