#!/bin/bash

for file in $@
  do
    width=`identify -format "%w" $file`
    height=`identify -format "%h" $file`
    if [[ $width < $height ]]; then
      convert -thumbnail 62x87! $file ../t_$file
    else
      convert -thumbnail 87x62! -rotate "90" $file ../t_$file
    fi
  done