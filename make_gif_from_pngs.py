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
for png in pngs.split("\n"):
  if ("x"+png != "x"):
    png            = re.sub(r'^\.\/', '', png)
    png_pieces     = png.split("/")
    setname        = png_pieces[0]
    png_subdir     = png_pieces[1]
    png_filename   = png_pieces[2]

    gif_filename   = png_filename.replace(".png", ".gif")
    t_gif_filename = "t_" + gif_filename

    ##
    ## Only gif images are supported in the large directory.
    ## "large" is used by the holotable app, so we will respect that requirement.
    ##
    print("  * ["+png+"]")
    print("    ** set.....: ["+setname+"]")
    print("    ** subdir..: ["+png_subdir+"]")
    print("    ** filename: ["+png_filename+"]")

    if (png_subdir == "hires"):
      print("       *** png already in hires dir")
    else:
      if (os.path.isfile(setname+"/hires/"+png_filename)):
        print("       *** png exists")
      else:
        print("       *** Moving png to hires")
        dewit="mkdir -p "+setname+"/hires"
        print("           "+dewit)
        os.popen(dewit)

        dewit="mv "+png+" "+setname+"/hires"
        print("           "+dewit)
        os.popen(dewit)

    if (os.path.isfile(setname+"/large/"+gif_filename)):
      print("       *** gif exists")
    else:
      print("       *** Generating gif")
      dewit="convert -quality 120 -resize 745x1039 "+setname+"/hires/"+png_filename+" "+setname+"/large/"+gif_filename
      print("           "+dewit)
      os.popen(dewit)

    if (os.path.isfile(setname+"/"+t_gif_filename)):
      print("       *** t_gif exists")
    else:
      print("       *** Generating t_gif")
      dewit="convert -quality 72 -resize 67x87 "+setname+"/large/"+gif_filename+" "+setname+"/"+t_gif_filename
      print("           "+dewit)
      if (not os.path.isfile(setname+"/large/"+gif_filename)):
        ##
        ## The large file may not be available before the next convert command is run.
        ## Give a 2 second sleep to give the filesystem time to catch up.
        ##
        time.sleep(2)
      os.popen(dewit)


print("\ndone.\n")

