import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(46, 41)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(178, 164)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "mutifourms"
		self.ResumeLayout(False)

