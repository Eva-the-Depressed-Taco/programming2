import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(243, 69)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(349, 69)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(0, 284)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(146, 24)
		self._checkBox1.TabIndex = 2
		self._checkBox1.Text = "I check useless boxxes "
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(93, 121)
		self._button1.Name = "button1"
		self._button1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 3
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(138, 69)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Enter text"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.PaleVioletRed
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Location = System.Drawing.Point(244, 96)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(138, 96)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 7
		self._label1.Text = "anogram?"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(400, 254)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "STRint2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		word = self._textBox1.Text
		anyo = self._textBox2.Text
		word = word.lower()
		anyo = anyo.lower()
		
		if len(word) != len(anyo):
			self._label3.Text = "Nah"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				index = anyo.index(c)
				
				if index != -1:
					anyo = anyo[0:index] + anyo[index+1:]
				else:
					self._label3.Text = "Nah"
		self._label3.Text = "Nah"
		