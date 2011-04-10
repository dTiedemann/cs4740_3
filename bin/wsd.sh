#!/bin/bash
#Run this like so
#score2csv <predictions> <key>
../classify.py

#Convert to a nice format
../scoring/scorer2 $1 $2  -v|sed -n -e 's/^score for //p'|sed -e 's/: /,/' -e 's/^.*_/"/' -e 's/.bnc./.bnc","/' #|
#Consider using the predictions file as an identifier for the treatment combination