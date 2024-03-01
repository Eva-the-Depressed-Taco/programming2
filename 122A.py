import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
  def __init__(self):
    self.InitializeComponent()

  def InitializeComponent(self):
    self._button1 = System.Windows.Forms.Button()
    self._listBox1 = System.Windows.Forms.ListBox()
    self.SuspendLayout()
    # 
    # button1
    # 
    self._button1.Location = System.Drawing.Point(33, 66)
    self._button1.Name = "button1"
    self._button1.Size = System.Drawing.Size(75, 23)
    self._button1.TabIndex = 0
    self._button1.Text = "button1"
    self._button1.UseVisualStyleBackColor = True
    self._button1.Click += self.Button1Click
    # 
    # listBox1
    # 
    self._listBox1.FormattingEnabled = True
    self._listBox1.Location = System.Drawing.Point(141, 54)
    self._listBox1.Name = "listBox1"
    self._listBox1.Size = System.Drawing.Size(239, 186)
    self._listBox1.TabIndex = 1
    # 
    # MainForm
    # 
    self.ClientSize = System.Drawing.Size(681, 545)
    self.Controls.Add(self._listBox1)
    self.Controls.Add(self._button1)
    self.Name = "MainForm"
    self.Text = "p122a"
    self.ResumeLayout(False)


  def Button1Click(self, sender, e):
    num = 1
    for i in range(50):
      self._listBox1.Items.Add(str(num) + "\t" +  str(num*num) + "\t" + str(round(math.sqrt(num), 3)))
      num+=1

