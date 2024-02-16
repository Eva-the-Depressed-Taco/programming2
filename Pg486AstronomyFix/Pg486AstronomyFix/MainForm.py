import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._panel1 = System.Windows.Forms.Panel()
		self._label1 = System.Windows.Forms.Label()
		self._button9 = System.Windows.Forms.Button()
		self._panel1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(327, 173)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Neptune"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(235, 110)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Earth"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(142, 110)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "venus"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(327, 110)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 23)
		self._button4.TabIndex = 3
		self._button4.Text = "Mars"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(48, 173)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(75, 23)
		self._button5.TabIndex = 4
		self._button5.Text = "Jupiter"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(142, 173)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(75, 23)
		self._button6.TabIndex = 5
		self._button6.Text = "Saturn"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(235, 173)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(75, 23)
		self._button7.TabIndex = 6
		self._button7.Text = "Uranus"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.Location = System.Drawing.Point(48, 110)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(75, 23)
		self._button8.TabIndex = 7
		self._button8.Text = "Mercury"
		self._button8.UseVisualStyleBackColor = True
		self._button8.Click += self.Button8Click
		# 
		# panel1
		# 
		self._panel1.BackColor = System.Drawing.Color.White
		self._panel1.Controls.Add(self._label1)
		self._panel1.Location = System.Drawing.Point(74, 255)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(375, 162)
		self._panel1.TabIndex = 8
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(19, 4)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(341, 150)
		self._label1.TabIndex = 0
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.SandyBrown
		self._button9.Location = System.Drawing.Point(476, 420)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(75, 21)
		self._button9.TabIndex = 9
		self._button9.Text = "pluto"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self.ClientSize = System.Drawing.Size(598, 439)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._panel1)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg486AstronomyFix"
		self._panel1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Neptune \n     Type Terrestrial \n    Average distance from the sun 30.0611 AU AU\n    Mass 4.87 × 10^24 kg\n    Surface temperature -216°C"

	def Button3Click(self, sender, e):
		self._label1.Text = "venus \n     Type Terrestrial \n    Average distance from the sun 0.7233 AU\n    Mass 4.87 × 10^24 kg\n    Surface temperature 1472°C"
	def Button2Click(self, sender, e):
		self._label1.Text = "Earth \n     Type Terrestrial \n    Average distance from the sun 1 AU\n    Mass 5.967 × 10^24  kg\n    Surface temperature -50 - 50C"	

	def Button4Click(self, sender, e):
		self._label1.Text = "mars \n     Type Terrestrial \n    Average distance from the sun 1.5237 AU\n    Mass  0.6424 × 10^24 kg kg\n    Surface temperature –140°C to 20°C"

	def Button5Click(self, sender, e):
		self._label1.Text = "Jupiter \n     Type Jovian \n    Average distance from the sun 5.2028 AU\n    Mass 1.899 × 10^27 kg kg\n    Surface temperature -120°C"


	def Button6Click(self, sender, e):
		self._label1.Text = "Saturn \n     Type Jovian \n    Average distance from the sun 9.5388 AU\n    Mass 5.69 × 10^26 kg kg\n    Surface temperature -180°C"
	def Button7Click(self, sender, e):
		self._label1.Text = "Uranuse \n     Type jovain \n    Average distance from the sun 19.18 AU AU\n    Mass 8.69 × 10^25 kg kg\n    Surface temperature -220°C"

	def Button8Click(self, sender, e):
		self._label1.Text = "Mercury \n     Type Terrestrial \n    Average distance from the sun 0.387 AU\n    Mass 3.31 × 10^23 kg\n    Surface temperature –173°C to 430°C"

	def Button9Click(self, sender, e):
		self._label1.Text = "Error, the planet you have selected is no longer a planet"