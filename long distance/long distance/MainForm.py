import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._button4 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(160, 85)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(53, 81)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "minutes"
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(30, 309)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 20)
		self._button1.TabIndex = 2
		self._button1.Text = "day"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(146, 219)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "evening"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(260, 219)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 4
		self._button3.Text = "of peak"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(111, 306)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(53, 219)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 23)
		self._button4.TabIndex = 6
		self._button4.Text = "calcualte"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self.ClientSize = System.Drawing.Size(578, 407)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "long distance"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		mins = str(self._textBox1.Text)
		r = 0
		cost = mins * r
		self._label2.Text = str(cost)

	def Button4Click(self, sender, e):
		day = True
		evening = False
		ofpeak = False
		r = 0.7

	def Button2Click(self, sender, e):
		day = False
		evening = True
		ofpeak = False
		r = 0.12
	def Button3Click(self, sender, e):
		day = False
		evening = False
		ofpeak = True
		r = 0.05