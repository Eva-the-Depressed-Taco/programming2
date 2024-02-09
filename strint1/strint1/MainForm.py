import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(39, 56)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(39, 111)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "label2"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(176, 56)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(39, 203)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(86, 66)
		self._button1.TabIndex = 4
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(176, 203)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 66)
		self._button2.TabIndex = 5
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(340, 203)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 66)
		self._button3.TabIndex = 6
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(176, 114)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 7
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(199, 151)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 8
		self._label3.Text = "label3"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self.ClientSize = System.Drawing.Size(546, 364)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "strint1"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		mystr = self._textBox1.Text.lower()
		for lcv in range(len(mystr)):
			for lcv2 in range(lcv+1, len(mystr)):
				letter1 = mystr(lcv)
				letter2 = mystr(lcv2)
				if letter1 == letter2:
					self._label3.Text == letter2 + ""
		
		
	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""