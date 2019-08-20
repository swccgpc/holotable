#!/bin/bash

for dir in $@
  do
    echo "Changing to directory $dir"
    pushd $dir
     for file in *.gif
       do
         width=`identify -format "%w" $file`
         height=`identify -format "%h" $file`
         if [[ $width < $height ]]; then
           convert -thumbnail 62x87! $file ../t_$file
         else
           convert -thumbnail 87x62! -rotate "90" $file ../t_$file
         fi
       done
    popd
    echo "Done with directory $dir"
  done