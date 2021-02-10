#!/bin/bash

bunzip2 -c Images-HT/listmd5.bz2 > serverimagelist.dat
cp Images-HT/listmd5.bz2 imagelist.tmp.bz2
zip -9 latest.zip \
  darkside.cdf lightside.cdf \
  *.gif \
  imagelist.tmp.bz2 \
  serverimagelist.dat
