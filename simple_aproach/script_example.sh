#!/bin/sh

pdftotext $1 $2
espeak --stdout -f $2 > output.mp3
rm $2
