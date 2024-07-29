#!/bin/bash

for i in *.aac ; do echo "$i" && ffmpeg -i $i  $i.mp3 ; done
