#!/usr/bin/bash
hashfile=./lightside.cdf

rm -f $hashfile.bz2

bzip2 -k ./$hashfile

echo "Remember to update the Dark CDF version number and file hash in version.dat"

sha256sum $hashfile.bz2

hashfile=./darkside.cdf

rm -f $hashfile.bz2

bzip2 -k ./$hashfile

echo "Remember to update the Light CDF version number and file hash in version.dat"

sha256sum $hashfile.bz2
