import math
from engine.libraries import out

def validate():
  out.output("Successfully imported", "math.py")
  
def sin(float):
  s = math.sin(float % 360)
  
  return s

def cos(float):
  c = math.cos(float % 360)
  
  return c

def distance(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  dist = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

  return dist