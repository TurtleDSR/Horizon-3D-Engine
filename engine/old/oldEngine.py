print("")
print("running old rendering engine")
  
import turtle
import math
import os
  
t = turtle.Turtle()
screen = turtle.Screen()



def render(focalZoom, tick):
  t.clear()
  t.ht()
  turtle.tracer(0, 0)
  
  renderObjects(focalZoom, tick)


def finalizeRender():
  turtle.update()

  
def lineRender(p1, p2, zoom):
  p1x, p1y, p1z = p1
  p2x, p2y, p2z = p2
  
  t.penup()
  t.goto((p1x / p1z) * zoom, (p1y / p1z) * zoom)
  t.pendown()
  t.goto((p2x / p2z) * zoom, (p2y / p2z) * zoom)

def zRot(point, centerPoint, angle):
  pointx, pointy, pointz = point
  centerx, centery, centerz = centerPoint
  
  s = math.sin((angle % 360))
 
  c = math.cos((angle % 360))
 
  x = ((pointx - centerx) * c) - ((pointy - centery) * s) + centerx
  y = ((pointx - centerx) * s) + ((pointy - centery) * c) + centery
  z = pointz
 
  outpoint = x, y, z
  return(outpoint)

def xRot(point, centerPoint, angle):
  pointx, pointy, pointz = point
  x, y, z = point
  if not (angle % 360) == 0:
      
    centerx, centery, centerz = centerPoint
    
    s = math.sin((angle % 360))
  
    c = math.cos((angle % 360))

    x = pointx
    y = ((pointy - centery) * c) - ((pointz - centerz) * s) + centery
    z = ((pointy - centery) * s) + ((pointz - centerz) * c) + centerz

  outpoint = x, y, z
  return(outpoint)
    
def cubeRender(x, y, z, w, h, l, xr, yr, zr, focalZoom):
   w, h, l = w / 2, h / 2, l / 2
   cp = (x, y, z)
    
   rectRender((x - w, y - h, z - l),(x - w, y + h, z - l ),(x + w, y + h, z - l),(x + w, y - h, z - l), cp, xr, yr, zr, focalZoom)
   rectRender((x - w, y - h, z + l),(x - w, y + h, z + l ),(x + w, y + h, z + l),(x + w, y - h, z + l), cp, xr, yr, zr, focalZoom)
   rectRender((x - w, y - h, z - l),(x - w, y + h, z - l ),(x - w, y + h, z + l),(x - w, y - h, z + l), cp, xr, yr, zr, focalZoom)
   rectRender((x + w, y - h, z - l),(x + w, y + h, z - l ),(x + w, y + h, z + l),(x + w, y - h, z + l), cp, xr, yr, zr, focalZoom)
  

def rectRender(p1, p2, p3, p4, cp, rx, ry, rz, zoom):
  np1, np2, np3, np4 = p1, p2, p3, p4
    
  np1 = zRot(p1, cp, rz)
  np2 = zRot(p2, cp, rz)
  np3 = zRot(p3, cp, rz)
  np4 = zRot(p4, cp, rz)
    
  np1 = xRot(np1, cp, rx)
  np2 = xRot(np2, cp, rx)
  np3 = xRot(np3, cp, rx)
  np4 = xRot(np4, cp, rx)
    
  lineRender(np1, np2, zoom)
  lineRender(np2, np3, zoom)
  lineRender(np3, np4, zoom)
  lineRender(np4, np1, zoom)


def renderObjects(focalZoom, tick):
  cubeRender(0, 0, 150, 100, 100, 100, (tick / 100), (tick / 100), (tick / 100), focalZoom)


def engineLoop():
  tick = 0
  newtick = 0
  while True:
    newtick = update(tick)
    tick = newtick
      
def update(ticks):
  focalZoom = 100
  render(focalZoom, ticks)
  finalizeRender()

  clearConsole()
    
  print('"running old rendering engine"')
  print("tick", ticks)
  return ticks + 1

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)
  
  
engineLoop()