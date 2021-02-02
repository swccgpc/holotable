#!/usr/bin/bash
hashfile=./Images-HT/listmd5

rm -f $hashfile $hashfile.bz2

date "+version %Y%m%d" > $hashfile

#echo "urlpath download/downloads/cards" >> $hashfile
echo "urlpath https://raw.githubusercontent.com/swccgpc/holotable/master/Images-HT" >> $hashfile

(cd ./Images-HT && ls *.gif | xargs -n 1 md5sum) | awk '{print "MD5 ("$2") = "$1}' >> $hashfile
find Images-HT/starwars -name "*.gif" | xargs -n 1 md5sum | awk '{print "MD5 ("$2") = "$1}' >> $hashfile

bzip2 -k $hashfile

echo "Remember to update the version number and file hash in version.dat"

sha256sum $hashfile.bz2
