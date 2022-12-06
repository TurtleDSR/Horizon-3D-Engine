'''

useless file that just needs to be here for everything to work.

'''

import os
os.system('clear')
from engine.libraries import out

runNew = 1 #keep as 1 unless you want a useless laggy mess rendered

if runNew == 1:

  out.output("attempting to load engine", "main.py")
  from engine.main import engine
  engine = engine

else:

  out.output("attempting to load old engine", "main.py")
  from engine.old import oldEngine
  engine = oldEngine