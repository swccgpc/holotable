#!/usr/bin/env python3

import os
import re
import time

if not re.match(r'.*\/starwars$', os.getcwd()):
  print("Changing to Images-HT/starwars directory to look for pngs")
  os.chdir("Images-HT/starwars")

if not re.match(r'.*\/starwars$', os.getcwd()):
  print("can not find the Images-HT/starwars directory... bailing out.")
  exit(1)

print("\nFinding pngs \n")
pngs = os.popen('find -iname \*.png').read()
pngs = pngs.split("\n")
pngs.sort()

for png in pngs:
  if ("x"+png != "x"):
    png            = re.sub(r'^\.\/', '', png)
    png_pieces     = png.split("/")
    setname        = png_pieces[0]
    png_subdir     = png_pieces[1]
    png_filename   = png_pieces[2]
    gif_filename   = png_filename.replace(".png", ".gif")

    hires_png_filename  = setname + "/hires/" + png_filename
    large_png_filename  = setname + "/large/" + png_filename
    large_gif_filename  = setname + "/large/" + gif_filename
    t_gif_filename      = setname + "/"       + "t_" + gif_filename

    print("\n  * [" + png + "]")
    print("    ** set.....: [" + setname + "]")
    print("    ** subdir..: [" + png_subdir + "]")
    print("    ** filename: [" + png_filename + "]")

    if (png_subdir == "hires"):

      print("       *** hires png source....: " + hires_png_filename)

      dewit="mkdir -p "+setname+"/large"
      os.popen(dewit)

      print("       *** Generating large gif: " + large_gif_filename)
      dewit="convert -quality 120 -resize 745x1039 " + hires_png_filename + " " + large_gif_filename
      os.popen(dewit)

      #print("       *** Generating large png: " + large_png_filename)
      #dewit="convert -quality 120 -resize 745x1039 " + hires_png_filename + " " + large_png_filename
      #os.popen(dewit)

      print("       *** Generating t_gif....: " + t_gif_filename)
      dewit="convert -quality 120 -resize 67x87 " + large_gif_filename + " " + t_gif_filename
      os.popen(dewit)



    



print("\ndone.\n")

