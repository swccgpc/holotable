#!/bin/bash

cd Images-HT/

##
## version is a date.
## date is a YYYYmmdd
##
echo
echo "Populating Date Version"
echo
echo "version $(date +%Y%m%d)" > listmd5

##
## urlpath does not have a trailing slash.
## urlpath is combined with the index from find, below.
## CORRECT: https://raw.githubusercontent.com/swccgpc/holotable/master/Images-HT
## WRONG..: https://raw.githubusercontent.com/swccgpc/holotable/master/Images-HT/
##
echo
echo "Populating url pathf"
echo
echo "urlpath https://raw.githubusercontent.com/swccgpc/holotable/master/Images-HT" >> listmd5

##
## Index all cards and add to listmd5 file.
## Filenames should not have a prefix slash.
## CORRECT: starwars/DeathStarII-Dark/t_admiralchiraneau.gif
## WRONG..: /starwars/DeathStarII-Dark/t_admiralchiraneau.gif
##
echo
echo "Indexing gif images"
echo
find -iname \*.gif -exec md5sum {} \; | awk '{
  gsub(/^\.\//, "", $2);
  print "MD5 ("$2") = "$1;
}' | tee -a listmd5

##
## compress with bzip2
##
if [ -f listmd5.bz2 ]; then
  echo
  echo "Removing old listmd5.bz2"
  echo
  rm -f listmd5.bz2
fi
echo
echo "Compressing with bzip2"
echo
bzip2 -k listmd5

cd ..

