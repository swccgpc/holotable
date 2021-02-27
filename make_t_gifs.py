#!/usr/bin/env python3

import os
import re
import time

def make_t_gifs(subdir="starwars"):
  if not re.match(r'.*\/'+subdir+'$', os.getcwd()):
    print("Changing to Images-HT/"+subdir+" directory to look for gifs")
    os.chdir("Images-HT/"+subdir)

  if not re.match(r'.*\/'+subdir+'$', os.getcwd()):
    print("can not find the Images-HT/"+subdir+" directory... bailing out.")
    exit(1)

  print("\nFinding gifs \n")
  pngs = os.popen('find -not -iname t_\*.gif -type f | grep "large"').read()
  for png in pngs.split("\n"):
    if ("x"+png != "x"):
      png            = re.sub(r'^\.\/', '', png)
      png_pieces     = png.split("/")
      setname        = png_pieces[0]
      png_subdir     = png_pieces[1]
      png_filename   = png_pieces[2]

      gif_filename   = png_filename.replace(".png", ".gif")
      t_gif_filename = "t_" + gif_filename

      print("  * ["+png+"]")
      print("    ** set.....: ["+setname+"]")
      print("    ** subdir..: ["+png_subdir+"]")
      print("    ** filename: ["+png_filename+"]")

      if (os.path.isfile(setname+"/"+t_gif_filename)):
        print("       *** t_gif exists")
      else:
        print("       *** Generating t_gif")
        dewit="convert -quality 72 -resize 67x87 "+setname+"/large/"+gif_filename+" "+setname+"/"+t_gif_filename
        print("           "+dewit)
        os.popen(dewit)

  os.chdir("../..")


make_t_gifs("legacy")
make_t_gifs("starwars")

print("\ndone.\n")

