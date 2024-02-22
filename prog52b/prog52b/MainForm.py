import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(77, 156)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label1.Location = System.Drawing.Point(89, 186)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label2.Location = System.Drawing.Point(89, 218)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "label2"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(28, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(28, 64)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(28, 90)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 5
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(28, 38)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog52b"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		n1 = int(self._textBox1.Text)
		n2 = int(self._textBox2.Text)
		n3 = int(self._textBox3.Text)
		n4 = ints(self._textBox4.Text)
		sum = n1 + n2 + n3 + n4
		ave = sum / 4
		self._label1.Text = str(sum)
		self._label2.Text = str(ave)