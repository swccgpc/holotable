#!/usr/bin/env python3

import os
import re
import time

print("\nFinding files \n")
os.chdir("Images-HT/")
fils = os.popen('find -type f').read()
for fil in fils.split("\n"):
  fil_pieces = fil.split("/")
  filename   = fil_pieces[len(fil_pieces)-1]
  filename_l = filename.lower().replace("'", "").replace("_", "").replace(" ", "")
  if ("x"+fil != "x"):
    if ((filename != filename_l) and
        ("-title" not in filename) and
        ("CardBack.gif" not in filename) and
        ("t_" not in filename)
        ("_ai" not in filename)
       ):
      print("  * ["+filename+"]: renaming to ["+filename_l+"]")
      to = fil.replace(filename, filename_l)
      dewit = "git mv -f \""+fil+"\" \""+to+"\""
      print("    "+dewit)
      os.popen(dewit)
      time.sleep(2)

