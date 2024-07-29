#!/bin/bash

for i in *.txt ; do echo "$i" && pandoc -s $i -o $i.docx ; done
