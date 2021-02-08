#!/usr/bin/env python3

import pathlib
import datetime
import time
import os
import re

from hashlib import sha256

def hash_file(filename):
  #with open(filename, mode='rb') as file:
  #  fileContent = file.read()
  #print(sha256(fileContent).hexdigest())
  r = os.popen('sha256sum '+filename).read().replace("\n", "")
  return re.sub(r' +.*$', "", r)

def get_version_from_filename(filename):
  s = re.split(r'[-_]+', filename)
  return s[1]

def get_mtime_from_file(filename):

  fname = pathlib.Path(filename)
  mtime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
  ctime = datetime.datetime.fromtimestamp(fname.stat().st_ctime)
  #print("modified:",mtime,"(",mtime.strftime("%Y%m%d"),")")
  #print("created.:",ctime,"(",ctime.strftime("%Y%m%d"),")")
  return


ht_windows_filename = "holotable-0.9.10_update.exe"
ht_linux_filename   = "holotable-0.9.9_update_linux.tar.bz2"

ht_windows_version = get_version_from_filename(ht_windows_filename)
ht_windows_sha256  = hash_file(ht_windows_filename)

ht_linux_version   = get_version_from_filename(ht_linux_filename)
ht_linux_sha256    = hash_file(ht_linux_filename)

listmd5_bz2_filename = 'Images-HT/listmd5.bz2'
listmd5_bz2_sha256   = hash_file(listmd5_bz2_filename)
listmd5_bz2_version  = os.popen('head -n 1 Images-HT/listmd5 | grep "^version"').read().replace("version ", "").replace("\n", "")
#listmd5_bz2_version  = get_mtime_from_file('Images-HT/listmd5')

lightside_cdf_bz2_filename = "lightside.cdf.bz2"
lightside_cdf_bz2_sha256   = hash_file("lightside.cdf.bz2")
lightside_cdf_bz2_version  = os.popen('head -n 1 lightside.cdf | grep "^version"').read().replace("version ", "").replace("\n", "")
#lightside_cdf_bz2_version  = get_mtime_from_file(lightside_cdf_bz2_filename)

darkside_cdf_bz2_sha256    = hash_file("darkside.cdf.bz2")
darkside_cdf_bz2_filename  = "darkside.cdf.bz2"
darkside_cdf_bz2_version   = os.popen('head -n 1 darkside.cdf | grep "^version"').read().replace("version ", "").replace("\n", "")
#darkside_cdf_bz2_version   = get_mtime_from_file(darkside_cdf_bz2_filename)

version_dat = {
  'latest':                 ht_windows_version,
  'Light CDF':              { 'version':lightside_cdf_bz2_version, 'sha256':lightside_cdf_bz2_sha256, 'src':lightside_cdf_bz2_filename },
  'Dark CDF':               { 'version':darkside_cdf_bz2_version,  'sha256':darkside_cdf_bz2_sha256,  'src':darkside_cdf_bz2_filename },
  'Holotable Windows exe':  { 'version':ht_windows_version,        'sha256':ht_windows_sha256,        'src':ht_windows_filename },
  'Holotable Linux unpack': { 'version':ht_linux_version,          'sha256':ht_linux_sha256,          'src':ht_linux_filename },
  'images':                 { 'version':listmd5_bz2_version,       'sha256':listmd5_bz2_sha256,       'src':listmd5_bz2_filename },
  'imagelisturl':           { 'version':listmd5_bz2_version,       'sha256':listmd5_bz2_sha256,       'src':'https://raw.githubusercontent.com/swccgpc/holotable/master/'+listmd5_bz2_filename },
}


fh = open("version.dat", "w")
fh.write(version_dat['latest']+"\n")

fh.write("Light CDF "+version_dat['Light CDF']['version']+" "+version_dat['Light CDF']['src']+" SHA256:"+version_dat['Light CDF']['sha256']+"\n")
fh.write("Dark CDF " +version_dat['Dark CDF']['version'] +" "+version_dat['Dark CDF']['src'] +" SHA256:"+version_dat['Dark CDF']['sha256'] +"\n")

fh.write("Holotable Windows exe " +version_dat['Holotable Windows exe']['version'] +" "+version_dat['Holotable Windows exe']['src']+" SHA256:"+version_dat['Holotable Windows exe']['sha256']+"\n")
fh.write("Holotable Linux unpack "+version_dat['Holotable Linux unpack']['version']+" "+version_dat['Holotable Linux unpack']['src']+" SHA256:"+version_dat['Holotable Linux unpack']['sha256']+"\n")

fh.write("images "+version_dat['images']['version']+" "+version_dat['images']['src']+" SHA256:"+version_dat['images']['sha256']+"\n")
fh.write("imagelisturl "+version_dat['imagelisturl']['version']+" "+version_dat['imagelisturl']['src']+" SHA256:"+version_dat['imagelisturl']['sha256']+"\n")

fh.close

