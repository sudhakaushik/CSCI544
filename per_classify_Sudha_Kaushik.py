import sys
import os
import pickle

from collections import defaultdict

filename = sys.argv[1]

op_filename = sys.argv[2]

word_weight = defaultdict()

b = 0
#i = 1

word_weight =  pickle.load( open( "per_model.txt", "rb" ) )

b = int(word_weight["bias_value"])
#print(word_weight)
#f = open('/Users/sudhakaushik/Desktop/NLP/HW2/per_model.txt', 'r', encoding='latin1')
#for line in f:
    #print(line)
#    if (i == 1):
#        words = line.split()
#        b = int(words[1])
#        #print(vocab_size)
#        i = i+1
#    else:
#        words = line.split()
#        word_weight[words[0]] = words[1]
#f.close()

alpha = 0

op = open(op_filename, 'w', encoding='latin1')

for subdir, dirs, files in os.walk(filename):
    for file in files:
        if file[len(file)-3:len(file)] == "txt":
            with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                alpha = 0
                for line in f:
                    #print(line)
                    words = line.split()
                    #print(words)
                    for word in words:
                        #print(word)
                        weight = word_weight.get(word,'fail')
                        if weight == 'fail':
                            continue
                        alpha += int(weight)

                alpha += b
                #print(alpha);
                if alpha > 0:
                    op.write('SAD' + ' ' + os.path.join(subdir, file) + '\n')
                else:
                    op.write('HAPPY' + ' ' + os.path.join(subdir, file) + '\n')
