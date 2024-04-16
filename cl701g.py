class person:
  def __init__(self, fn, ln):
    self._first = fn
    self._last = ln

  def getname(self):
    return self._first + '  ' + self._last


class sttudent(person):
  def __init__(self, fn, ln, gpa):
    super().__init__(fn, ln)
    self.gpa = gpa

class teacher(person):
  def __init__(self, fn, ln, numstu):
    super().__init__(fn, ln)
    self.numstu = numstu
class admin(person):
  def __init__(self, fn, ln, favw):
    super().__init__(fn, ln)
    self.numstu = favw
    
    
  