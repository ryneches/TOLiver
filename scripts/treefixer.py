#!/bin/env python
# usage : ./treefixer.py names.txt tree.newick > newtree.newick
# names.txt : oldname1 oldname2 oldname3 newname
import sys

r = {}

for line in open( sys.argv[1] ) :
    name = line.split()[-1]
    for target in line.split()[:-1] :
        r[target] = name

t = open( sys.argv[2] ).read()

for target,name in r.items() :
    t.replace( target, name )

print(t)
