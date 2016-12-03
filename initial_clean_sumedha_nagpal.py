import glob
import sys
import os
from collections import defaultdict
import json
import nltk
from nltk.stem.porter import *


dictionary = {}
path2 = sys.argv[2]
path1 = sys.argv[1]
song_filenames = sorted(glob.glob(os.path.join(path1, "*.txt")))
for songname in song_filenames:
	f = open(songname, 'r', encoding = "latin-1")
	allLines = f.read().split()
	for line in allLines:
		line = ''.join([c for c in line if c not in ('!', '?',',','.',')','(','[',']','{','}','-','_','\'',':',';','\"')])
		line = line.lower()
		stemmer = PorterStemmer()
		line = stemmer.stem(line)
		if(line in dictionary):
			dictionary[line] +=1
			
		else:
			dictionary[line] = 1	
			
outputfile = open(path2, 'w')
for k,v in dictionary.items():
	outputfile.write("Key_" + str(k) +'\t\t\tValue_' + str(v), end = '\n' )

outputfile.close()	