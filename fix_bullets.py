#!/usr/bin/env python3

import codecs


def fix_cdf_file_bullets(cdf_filename):

  print("Fixing Bullets in "+cdf_filename)
  proper_bullet = b'\x95'.decode('cp1252')

  print("  * Reading CDF File")
  fh  = codecs.open(cdf_filename, "rb", 'cp1252')
  txt = fh.read()
  fh.close

  print("  * Read Contents: "+str(type(txt)))

  print("  * Replacing known bad/invalid bullets")
  txt = txt.replace("ï¿½",  proper_bullet)
  txt = txt.replace("½",  proper_bullet)
  txt = txt.replace("¿",  proper_bullet)
  txt = txt.replace("ï",  proper_bullet)
  #for lin in txt.split("\n"):
  #  if "Death Star: War Room" in lin:
  #    print(lin[0:70])
  #  if "Vader's Lightsaber" in lin:
  #    print(lin[0:70])

  print("  * Writing CDF File")
  fh = codecs.open(cdf_filename, "w", 'cp1252')
  fh.write(txt)
  fh.close

  print("  * done.\n")


fix_cdf_file_bullets("darkside.cdf")
fix_cdf_file_bullets("lightside.cdf")
