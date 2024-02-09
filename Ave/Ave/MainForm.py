import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._button1.Location = System.Drawing.Point(83, 182)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "calcualte"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(69, 69)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(69, 121)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 2
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(69, 147)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 3
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(69, 95)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 4
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label1.Location = System.Drawing.Point(325, 206)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "averege  "
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label2.Location = System.Drawing.Point(325, 182)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "sum   "
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._button2.Location = System.Drawing.Point(83, 211)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._button3.Location = System.Drawing.Point(83, 240)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Purple
		self.ClientSize = System.Drawing.Size(724, 376)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Ave"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		n1 = int(self._textBox1.Text)
		n2 = int(self._textBox2.Text)
		n3 = int(self._textBox3.Text)
		n4 = int(self._textBox4.Text)
		T = n1 + n2 + n3 + n4
		A = T / 4
		self._label2.Text += str(T)
		self._label1.Text += str(A)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label1.Text = "Averege  "
		self._label2.Text = "Sum  "
		
		
		

	def Button3Click(self, sender, e):
		Application.Exit()