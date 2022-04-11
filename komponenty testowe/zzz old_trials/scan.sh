#!/bin/sh
BASEDIR="./data"
ls -A $BASEDIR > newfiles
DIRDIFF=$(diff oldfiles newfiles | cut -f 2 -d "")

for file in $DIRDIFF
do
echo $file
done