#!/usr/bin/env python3

import os
import re
from time import sleep

class CaseFixer():


  def generate_new_filename(self, fil):
    fil_pieces = fil.split("/")
    filename   = fil_pieces[len(fil_pieces)-1]
    filename_l = filename.lower().replace("'", "").replace("_", "").replace(" ", "")
    ##
    ## There is an exception to the rule with _ai filenames.
    ## Some _ai filenames even have numbers! _ai3.png
    ## This regex will find _ai and _aiX where X is a number.
    ## The star (*) means 0 more more occurances.
    ## The dollar sign means to match the end of the line.
    ## The pipe will match gif or png files.
    ##
    ai_sub_regex = re.compile(r'ai([0-9]*)\.(gif|png)$')
    filename_l = ai_sub_regex.sub('_ai\g<1>.\g<2>', filename_l)
    new_name = fil

    if ("x"+fil != "x"): # filename is empty
      if ((filename != filename_l) and # if the name is the same, it was already renamed.
          ("-title" not in filename) and # exception to the rule
          ("CardBack.gif" not in filename) and # exception to the rule
          ("t_" not in filename) # do not rename the wee cards
         ):
        new_name = fil.replace(filename, filename_l)
    return new_name


  def fix_them_all(self):
    print("\nFinding files \n")
    os.chdir("Images-HT/")
    fils = os.popen('find -type f').read()
    for fil in fils.split("\n"):
      new_fil = self.generate_new_filename(fil)
      if fil != new_fil:
        print("  * attempting to ["+fil+"]: renaming to ["+new_fil+"]")
        dewit = "git mv -f \""+fil+"\" \""+new_fil+"\""
        print("    "+dewit)
        os.popen(dewit)
        sleep(2)


##
## Ensure that if this file is loaded a class, it is not executed.
##
if __name__ == "__main__":
  cf = CaseFixer()
  cf.fix_them_all()






