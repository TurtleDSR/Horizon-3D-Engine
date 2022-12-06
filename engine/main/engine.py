'''
initialization
'''

import os

from engine.main import update
from engine.libraries import out
from engine.libraries import math

#os, update, out, math = os, update, out, math #just to get squiggles to go away


def initialize():
  
  return 0
  
def init():
  initialize()
  update.initialize()


'''
QOL scripts
'''


def output(message):
  out.output(message, "engine.py")


'''
Engine Loop
'''

def engine():
  engineLoop()


def engineLoop():
  while True:
    break








'''
run
'''

out.validate()
update.validate()
output("Engine initialized")
